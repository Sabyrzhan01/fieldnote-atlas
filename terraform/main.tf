terraform {
  required_version = ">= 1.5.0"
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

# Firewall rule allowing HTTP and Fieldnote Atlas web port
resource "google_compute_firewall" "allow_fieldnote" {
  name    = "allow-fieldnote-web"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["80", "443", "8091"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["fieldnote-atlas"]
}

# Free-Tier eligible e2-micro compute instance (GCP Always Free Tier in us-central1, us-west1, or us-east1)
resource "google_compute_instance" "fieldnote_app" {
  name         = "fieldnote-atlas-vm"
  machine_type = var.machine_type
  zone         = "${var.region}-a"
  tags         = ["fieldnote-atlas"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-12"
      size  = 25 # GB, within the 30 GB standard persistent disk Always Free tier
      type  = "pd-standard"
    }
  }

  network_interface {
    network = "default"
    access_config {
      // Ephemeral public IP
    }
  }

  metadata_startup_script = <<-EOF
    #!/bin/bash
    set -e
    exec > /var/log/startup-script.log 2>&1

    echo "[*] Updating system packages..."
    apt-get update -y
    apt-get install -y ca-certificates curl gnupg git

    echo "[*] Installing Docker engine..."
    install -m 0755 -d /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    chmod a+r /etc/apt/keyrings/docker.gpg

    echo \
      "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
      "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
      tee /etc/apt/sources.list.d/docker.list > /dev/null

    apt-get update -y
    apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

    systemctl enable --now docker

    echo "[*] Cloning Fieldnote Atlas repository..."
    mkdir -p /opt/fieldnote-atlas
    cd /opt/fieldnote-atlas
    git clone https://github.com/Sabyrzhan01/fieldnote-atlas.git .

    echo "[*] Starting Docker Compose stack..."
    docker compose up -d --build

    echo "[+] Fieldnote Atlas deployed successfully!"
  EOF

  labels = {
    app         = "fieldnote-atlas"
    environment = "freetier"
  }
}
