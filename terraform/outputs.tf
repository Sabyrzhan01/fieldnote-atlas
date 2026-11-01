output "instance_ip" {
  value       = google_compute_instance.fieldnote_app.network_interface[0].access_config[0].nat_ip
  description = "The public IPv4 address of the Fieldnote Atlas VM instance."
}

output "application_url" {
  value       = "http://${google_compute_instance.fieldnote_app.network_interface[0].access_config[0].nat_ip}:8091"
  description = "Live Fieldnote Atlas web application URL."
}

output "free_tier_notice" {
  value       = "Provisioned with 1x e2-micro instance in us-central1 and 25GB standard persistent disk to align with Google Cloud Free Tier / $300 trial credit allowances. Charges can apply if account quotas, network egress, or trial limits are exceeded; run 'terraform destroy' when not in use."
  description = "Google Cloud Free Tier and credit usage notice."
}
