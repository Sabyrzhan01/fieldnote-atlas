variable "project_id" {
  description = "GCP Project ID"
  type        = string
}

variable "region" {
  description = "GCP Region (Free-Tier eligible)"
  type        = string
  default     = "us-central1"
}

variable "container_image" {
  description = "Container image URI from Artifact Registry or GHCR"
  type        = string
  default     = "ghcr.io/sabyrzhan01/fieldnote-atlas:latest"
}

variable "db_user" {
  description = "PostgreSQL database username"
  type        = string
  default     = "fieldnote"
}

variable "db_password" {
  description = "PostgreSQL database password (injected via TF_VAR_db_password)"
  type        = string
  sensitive   = true
}

variable "billing_account_id" {
  description = "Optional GCP Billing Account ID for the $5/month budget alert"
  type        = string
  default     = ""
}
