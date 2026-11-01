# DevOps: AWS CloudFormation Free-Tier Production Deployment

**Labels:** `devops`, `aws`, `cloudformation`

## Goal
Deploy Fieldnote Atlas to Amazon Web Services using AWS CloudFormation, strictly adhering to Free Tier limits ($100 credit safety).

## Description
Provide an infrastructure-as-code AWS CloudFormation template:
- Compute: Free-tier eligible EC2 instance (`t2.micro` or `t3.micro`).
- Storage: 20GB gp3 EBS root volume (safely within the 30GB/month free tier).
- Networking: Security Group allowing inbound HTTP (80), HTTPS (443), Atlas Web (8091), and SSH (22).
- Automation: Cloud-init UserData script that installs Docker, Docker Compose, clones the repository, and launches the `docker-compose.yml` stack with PostgreSQL automatically.
- Cost Control: Strictly guards against paid AWS features to preserve free-tier credit status.

## Deliverables
- `aws/cloudformation.yaml`
- `aws/README.md` (Step-by-step AWS deployment and free-tier verification guide)

## Acceptance Criteria
- [x] CloudFormation template validates with AWS CLI (`aws cloudformation validate-template`).
- [x] Zero paid tier features enabled; strictly free tier parameters.
- [x] UserData automates Docker container deployment and PostgreSQL database setup.
