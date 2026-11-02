# Fieldnote Atlas — Production Infrastructure as Code (`infra/`)

This directory contains production-grade, **Free-Tier-compliant** Infrastructure-as-Code (IaC) definitions for both **AWS CloudFormation** (`infra/aws/template.yaml`) and **GCP Terraform** (`infra/gcp/*.tf`).

---

## 1. Cost Control & Free-Tier Guardrails

To guarantee **$0.00/month** cost within AWS Free Tier / GCP Free Credits:
- **Zero Paid Add-Ons**:
  - **No NAT Gateway** (uses Default VPC public subnets for ECS host; RDS restricted to `AppSecurityGroup` on port `5432`).
  - **No Application Load Balancer (ALB)** (direct container port mapping on EC2 `t3.micro` or serverless Cloud Run ingress).
  - **No Multi-AZ RDS** (`MultiAZ: false` on AWS `db.t3.micro`; `availability_type = "ZONAL"` on GCP `db-f1-micro`).
- **Automated Budget Alerts**:
  - **AWS**: `MonthlyCostBudget` (`AWS::Budgets::Budget`) configured at **$5.00/month** with an **80% ($4.00) email alert** to `AlertEmail`.
  - **GCP**: `google_billing_budget.free_tier_budget` configured at **$5.00/month** with threshold alerts at **50%, 80%, and 100%**.

| Resource | AWS (`infra/aws/template.yaml`) | GCP (`infra/gcp/*.tf`) | Monthly Expected Cost |
|---|---|---|---|
| **Compute** | ECS on 1× `t3.micro` (750 hrs/mo free tier) | Cloud Run v2 (`min_instance_count = 0`, 2M req/mo free) | **$0.00** (Free Tier) |
| **Database** | RDS PostgreSQL 16 `db.t3.micro` Single-AZ (750 hrs + 20GB free) | Cloud SQL Postgres 16 `db-f1-micro` Zonal | **$0.00** (Free Tier / Credits) |
| **Container Registry** | Amazon ECR (500 MB free + lifecycle policy keeping last 5 images) | Artifact Registry (500 MB free) | **$0.00** |
| **Secrets** | AWS Secrets Manager (`DatabaseSecret`, auto-generated 24-char password) | Terraform sensitive `TF_VAR_db_password` / Secret Manager | **<$0.40** or Free Credits |
| **Budget Alert** | `AWS::Budgets::Budget` ($5.00 cap) | `google_billing_budget` ($5.00 cap) | **$0.00** |

---

## 2. Option A: Deploy with AWS CloudFormation (`infra/aws/template.yaml`)

### Validate Template
```bash
aws cloudformation validate-template \
  --template-body file://infra/aws/template.yaml
```

### Deploy Stack
```bash
aws cloudformation deploy \
  --stack-name fieldnote-atlas-prod \
  --template-file infra/aws/template.yaml \
  --capabilities CAPABILITY_IAM \
  --parameter-overrides \
    EnvironmentName=fieldnote-atlas-prod \
    VpcId=vpc-xxxxxxxx \
    PublicSubnetIds=subnet-xxxx,subnet-yyyy \
    AlertEmail=your-email@example.com
```

### Tear Down Stack (Zero Residual Cost)
```bash
aws cloudformation delete-stack --stack-name fieldnote-atlas-prod
aws cloudformation wait stack-delete-complete --stack-name fieldnote-atlas-prod
```

---

## 3. Option B: Deploy with GCP Terraform (`infra/gcp/*.tf`)

### Initialize & Validate
```bash
cd infra/gcp
terraform init -backend=false
terraform validate
```

### Plan & Apply
```bash
export TF_VAR_project_id="your-gcp-project-id"
export TF_VAR_db_password="your-strong-db-password"
terraform plan -out=tfplan
terraform apply tfplan
```

### Tear Down Stack (Zero Residual Cost)
```bash
cd infra/gcp
terraform destroy -auto-approve
```
