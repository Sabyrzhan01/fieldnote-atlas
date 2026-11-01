# Google Cloud Platform Deployment Guide with Terraform (Free-Tier Sized)

This guide walks through deploying Fieldnote Atlas to Google Cloud Platform using Terraform as the Infrastructure-as-Code tool, sized to fit within Google Cloud's `$300` Free Trial credits and Always Free tier resource limits.

---

## GCP Free Tier & Credit Considerations
- **Compute:** 1× `e2-micro` instance in `us-central1`, `us-west1`, or `us-east1` (eligible for GCP's 1 non-preemptible `e2-micro` instance/month Always Free allowance on qualifying accounts).
- **Storage:** 25 GB standard persistent disk (`pd-standard`, within the 30 GB/month Always Free standard disk quota).
- **Network Egress & IPv4 Caveats:** Always Free includes 1 GB/month of North America outbound egress (excluding certain destinations); usage beyond free-tier allowances, external IP pricing changes, or running multiple instances will consume `$300` trial credits or incur billing. Always destroy resources (`terraform destroy`) when no longer needed.

---

## Prerequisites
1. [Google Cloud SDK (`gcloud`)](https://cloud.google.com/sdk/docs/install) installed.
2. [Terraform CLI](https://developer.hashicorp.com/terraform/downloads) (>= 1.5.0) installed.
3. An active GCP account with billing enabled (new accounts get \$300 in free credits).

---

## Deployment Steps

### 1. Authenticate with Google Cloud
```bash
# Log in to your Google Cloud account
gcloud auth login
gcloud auth application-default login

# Set your active project
gcloud config set project YOUR_PROJECT_ID
```

### 2. Configure Terraform Variables
```bash
cd terraform
cp terraform.tfvars.example terraform.tfvars
```
Edit `terraform.tfvars`:
```hcl
project_id   = "YOUR_ACTUAL_GCP_PROJECT_ID"
region       = "us-central1"
machine_type = "e2-micro"
```

### 3. Initialize and Apply Terraform
```bash
# Initialize Terraform provider plugins
terraform init

# Review planned infrastructure changes
terraform plan

# Provision resources
terraform apply -auto-approve
```

### 4. Access the Live Application
When Terraform finishes, it prints the outputs:
```text
Outputs:

application_url = "http://34.123.45.67:8091"
instance_ip = "34.123.45.67"
free_tier_notice = "Provisioned strictly within Google Cloud Always Free tier..."
```
Wait 2–3 minutes for the instance startup script to pull and boot the Docker container, then open:
`http://<instance_ip>:8091`

---

## Teardown
To cleanly destroy all provisioned GCP resources:
```bash
terraform destroy -auto-approve
```
