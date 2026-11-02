terraform {
  required_version = ">= 1.5.0"

  # Remote state backend (can be initialized with -backend-config or local fallback)
  backend "gcs" {
    bucket = "fieldnote-atlas-tfstate"
    prefix = "infra/gcp"
  }

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

# 1. Artifact Registry Repository for Fieldnote Atlas Docker images
resource "google_artifact_registry_repository" "fieldnote_repo" {
  location      = var.region
  repository_id = "fieldnote-atlas"
  description   = "Docker repository for Fieldnote Atlas multi-stage container"
  format        = "DOCKER"
}

# 2. Smallest-tier Cloud SQL for PostgreSQL 16 (db-f1-micro, Single-Zone)
resource "google_sql_database_instance" "postgres" {
  name             = "fieldnote-atlas-pg"
  database_version = "POSTGRES_16"
  region           = var.region

  settings {
    tier              = "db-f1-micro"
    availability_type = "ZONAL" # Single-zone for lowest cost
    disk_size         = 10
    disk_type         = "PD_HDD"
  }

  deletion_protection = false
}

resource "google_sql_database" "database" {
  name     = "fieldnote_atlas"
  instance = google_sql_database_instance.postgres.name
}

resource "google_sql_user" "user" {
  name     = var.db_user
  instance = google_sql_database_instance.postgres.name
  password = var.db_password
}

# 3. Cloud Run v2 Service (scales to zero, free-tier CPU/memory limits)
resource "google_cloud_run_v2_service" "app" {
  name     = "fieldnote-atlas"
  location = var.region
  ingress  = "INGRESS_TRAFFIC_ALL"

  template {
    scaling {
      min_instance_count = 0
      max_instance_count = 2
    }

    containers {
      image = var.container_image

      ports {
        container_port = 8000
      }

      resources {
        limits = {
          cpu    = "1"
          memory = "512Mi"
        }
      }

      env {
        name  = "DATABASE_URL"
        value = "postgresql+psycopg://${var.db_user}:${var.db_password}@/${google_sql_database.database.name}?host=/cloudsql/${google_sql_database_instance.postgres.connection_name}"
      }

      startup_probe {
        http_get {
          path = "/api/health"
          port = 8000
        }
        initial_delay_seconds = 5
        period_seconds        = 10
        failure_threshold     = 5
      }
    }
  }
}

resource "google_cloud_run_v2_service_iam_member" "public_invoker" {
  location = google_cloud_run_v2_service.app.location
  name     = google_cloud_run_v2_service.app.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}

# 4. GCP Billing Budget Alert ($5/month cap with 50%, 80%, and 100% alerts)
resource "google_billing_budget" "free_tier_budget" {
  count           = var.billing_account_id != "" ? 1 : 0
  billing_account = var.billing_account_id
  display_name    = "fieldnote-atlas-free-tier-budget"

  amount {
    specified_amount {
      currency_code = "USD"
      units         = "5"
    }
  }

  threshold_rules {
    threshold_percent = 0.5
  }
  threshold_rules {
    threshold_percent = 0.8
  }
  threshold_rules {
    threshold_percent = 1.0
  }
}
