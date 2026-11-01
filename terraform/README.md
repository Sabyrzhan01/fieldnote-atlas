# Google Cloud Platform Deployment Guide with Terraform (Strict Free Tier)

This guide walks through deploying Fieldnote Atlas to Google Cloud Platform using Terraform as the Infrastructure-as-Code tool, strictly utilizing the GCP Free Tier (consuming the \$300 credits and running within the Always Free tier).

---

## Free Tier Cost Guarantee
- **Compute:** 1× `e2-micro` instance per month in `us-central1`, `us-west1`, or `us-east1` (Always Free tier).
- **Storage:** 25 GB standard persistent disk (`pd-standard`, within the 30 GB/month Always Free quota).
- **Network Egress:** 1 GB free outbound traffic per month.
- **Credit Safety:** Safely uses the \$300 initial GCP trial credits with zero risk of overage.

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
