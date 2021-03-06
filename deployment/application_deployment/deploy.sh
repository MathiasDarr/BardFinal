
export AWS_ACCOUNT=$(aws sts get-caller-identity --query Account --output text)

cdk synth --require-approval never
cdk deploy --require-approval never

export PUBLIC_IP=$(aws cloudformation --region us-west-2 describe-stacks --stack-name DakobedBardStack | jq -r '.Stacks[].Outputs | reduce .[] as $i ({}; .[$i.OutputKey] = $i.OutputValue) | .bardip ')

