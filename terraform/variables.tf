variable "project_id" {
  type        = string
  description = "The Google Cloud Platform Project ID."
}

variable "region" {
  type        = string
  default     = "us-central1"
  description = "GCP Region (us-central1, us-west1, or us-east1 qualify for Always Free e2-micro tier)."
}

variable "machine_type" {
  type        = string
  default     = "e2-micro"
  description = "Free-tier eligible compute engine machine type (e2-micro)."
}
