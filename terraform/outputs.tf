output "instance_ip" {
  value       = google_compute_instance.fieldnote_app.network_interface[0].access_config[0].nat_ip
  description = "The public IPv4 address of the Fieldnote Atlas VM instance."
}

output "application_url" {
  value       = "http://${google_compute_instance.fieldnote_app.network_interface[0].access_config[0].nat_ip}:8091"
  description = "Live Fieldnote Atlas web application URL."
}

output "free_tier_notice" {
  value       = "Provisioned strictly within Google Cloud Always Free tier (1 e2-micro instance in us-central1 and 25GB standard persistent disk). Free of charge."
  description = "Free tier cost guarantee notice."
}
