# DevOps: Google Cloud Platform Terraform Free-Tier Production Deployment

**Labels:** `devops`, `gcp`, `terraform`

## Goal
Deploy Fieldnote Atlas to Google Cloud Platform using Terraform as the CloudFormation alternative, staying within the $300 free credits and Always Free tier.

## Description
Provide declarative Terraform configuration for GCP:
- Compute: Google Cloud Run (always free tier provides 2 million requests per month free) or Compute Engine `e2-micro` instance (Always Free eligible in `us-central1`, `us-west1`, or `us-east1`).
- Storage: Standard persistent disk up to 30GB.
- Network & Firewall: HTTP/HTTPS firewall rules for public web access.
- Automation: Startup script to run the Docker Compose stack.
- Variables and Outputs: Configurable region, project ID, and automated public IP output.

## Deliverables
- `terraform/main.tf`
- `terraform/variables.tf`
- `terraform/outputs.tf`
- `terraform/terraform.tfvars.example`
- `terraform/README.md` (Step-by-step GCP Terraform guide)

## Acceptance Criteria
- [x] Terraform scripts follow GCP best practices and free-tier allocation.
- [x] Cloud Run / Compute Engine configurations fully documented.
- [x] Variables and output URLs formatted cleanly.
