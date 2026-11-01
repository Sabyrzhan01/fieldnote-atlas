# AWS CloudFormation Deployment Guide (Strict Free Tier)

This deployment provisions a production-grade Fieldnote Atlas stack on Amazon Web Services using AWS CloudFormation, strictly adhering to the AWS Free Tier (ensuring \$0 expenditure and safely consuming the \$100 credit tier).

---

## Free Tier Cost Guarantee
- **Compute:** 1× `t2.micro` or `t3.micro` EC2 instance (750 hours/month free in AWS Free Tier).
- **Storage:** 20 GB gp3 EBS root volume (AWS provides 30 GB/month EBS for free).
- **Network Ingress:** Inbound HTTP (port 80 / 8091) is 100% free.
- **Database:** Runs inside PostgreSQL 16 container on the same instance with local persistent Docker volume.
- **Paid Features:** 0 paid features enabled. No Load Balancer, no NAT Gateway, no paid RDS instances.

---

## Deployment Steps

### Method 1: Using the AWS Management Console
1. Log in to the [AWS Management Console](https://console.aws.amazon.com/cloudformation).
2. Ensure you are in a free-tier eligible region (e.g. `us-east-1`, `us-east-2`, `us-west-2`, `eu-central-1`).
3. Navigate to **CloudFormation** → Click **Create stack** (with new resources).
4. Choose **Upload a template file** → Select `aws/cloudformation.yaml`.
5. Enter Stack details:
   - **Stack name:** `fieldnote-atlas`
   - **InstanceType:** `t2.micro` (or `t3.micro`)
   - **KeyName:** (Optional: select an existing EC2 keypair if you want SSH access, or leave blank).
6. Click **Next** → **Next** → Check "I acknowledge that AWS CloudFormation might create IAM resources" (if prompted) → Click **Submit**.
7. Wait 3–4 minutes for the stack status to reach `CREATE_COMPLETE`.
8. Click the **Outputs** tab to view your `ApplicationUrl` and `PublicIP`.
9. Open `http://<PublicIP>:8091/` in your web browser!

---

### Method 2: Using the AWS CLI
```bash
aws cloudformation create-stack \
  --stack-name fieldnote-atlas \
  --template-body file://aws/cloudformation.yaml \
  --parameters ParameterKey=InstanceType,ParameterValue=t2.micro \
  --region us-east-1

# Wait for stack completion:
aws cloudformation wait stack-create-complete --stack-name fieldnote-atlas --region us-east-1

# Retrieve the live public URL:
aws cloudformation describe-stacks \
  --stack-name fieldnote-atlas \
  --query "Stacks[0].Outputs[?OutputKey=='ApplicationUrl'].OutputValue" \
  --output text
```

---

## Verification & Management
- Access the running app: `http://<PublicIP>:8091/`
- API Health check: `http://<PublicIP>:8091/api/health`
- REST API data: `http://<PublicIP>:8091/api/atlas`

To delete the stack when done and terminate all resources:
```bash
aws cloudformation delete-stack --stack-name fieldnote-atlas --region us-east-1
```
