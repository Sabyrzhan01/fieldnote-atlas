# AWS CloudFormation Deployment Guide (Free-Tier Sized Architecture)

This deployment provisions a Fieldnote Atlas Docker Compose stack on Amazon Web Services using AWS CloudFormation, sized specifically for AWS Free Tier / Free Account credit limits (`$100` promotional/free-account credits) without enabling paid managed services.

---

## AWS Free Tier, Credits & Pricing Considerations
- **Compute:** 1× `t2.micro` or `t3.micro` EC2 instance (eligible for up to 750 hours/month for 12 months on qualifying AWS Free Tier accounts, or billed against available promotional credits).
- **Storage:** 20 GB `gp3` EBS root volume with `DeleteOnTermination: true` (within the 30 GB/month 12-month Free Tier EBS allowance on qualifying accounts).
- **Database:** Runs inside the `postgres:16-alpine` container on the same EC2 instance via Docker Compose rather than provisioning a separate RDS instance.
- **No Paid Add-on Services:** Does not provision Application Load Balancers, NAT Gateways, or Elastic IPs.
- **Important Billing & Public IPv4 Caveats:**
  - AWS does **not** guarantee `$0` billing automatically; actual cost depends on your AWS account's plan, age (12-month Free Tier eligibility vs. credit-based Free Account), region, and remaining promotional credits. See [AWS Free Tier guidance](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier.html).
  - **Public IPv4 Addressing:** AWS charges `$0.005/hour` for in-use public IPv4 addresses unless covered by active account credits or specific Free Tier allowances. See [AWS EC2 Instance Addressing & Public IPv4 pricing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html).
  - Always tear down the stack (`aws cloudformation delete-stack`) when finished testing to avoid exhausting hours or credits.

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
