

# Google Drive Setup
1. Create project Workbench-Sandbox (https://console.cloud.google.com/)
2. Create service account workbench-sandbox
3. Create Json key and download. 
4. Convert it to a token using google token generator python file
1. Share the drive folder having knowledge documents with service user workbench-sandbox@workbench-sandbox.iam.gserviceaccount.com on gdrive
2. https://docs.langflow.org/integrations-setup-google-oauth-langflow
4. OAuth Token does not works with langflow so ignore that in the link above

# authenticate cli (Must have user keys) : 
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 533267168457.dkr.ecr.us-east-1.amazonaws.com

# Tag local image
docker tag langflow_frontend:1.3.4.0 533267168457.dkr.ecr.us-east-1.amazonaws.com/kendralabs/workbench-frontend:1.3.4.1

# Push local image
docker push 533267168457.dkr.ecr.us-east-1.amazonaws.com/kendralabs/workbench-frontend:1.3.4.1

# Run Dockers Locally : 
# Backend : 
 docker run -p 7860:7860 \                                                                                              
  -e LANGFLOW_AUTO_LOGIN=false \
  -e LANGFLOW_CONFIG_DIR=app/langflow \
  -e LANGFLOW_DATABASE_URL="postgresql://postgresadmin:P0stgre\$007@workbench-sandbox-db-02.c10y6i62wvap.us-east-1.rds.amazonaws.com:5432/workbenchsandbox01" \
  -e LANGFLOW_SUPERUSER=superadmin \
  -e LANGFLOW_SUPERUSER_PASSWORD=superadmin123 \
  langflow_backend:1.3.4.0
# Frontend 
docker run --name langflow-frontend -p 8080:8080 -e BACKEND_URL="http://rj4pmw466h.us-east-1.awsapprunner.com" -e FRONTEND_PORT=8080  langflow_frontend:1.3.4.0