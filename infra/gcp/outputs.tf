output "cloud_run_url" {
  description = "Public HTTPS URL of the deployed Cloud Run service"
  value       = google_cloud_run_v2_service.app.uri
}

output "artifact_registry_repo" {
  description = "Artifact Registry Docker repository ID"
  value       = google_artifact_registry_repository.fieldnote_repo.id
}

output "cloud_sql_connection_name" {
  description = "Cloud SQL PostgreSQL 16 instance connection name"
  value       = google_sql_database_instance.postgres.connection_name
}
