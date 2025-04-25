# FastAPI Deployment On gcloud

1. Launch gcloud

    ```
    gcloud init
    ```

2. Create config or choose one

3. Create project or choose one

4. Export your project id variable name

    ```
    export PROJECT_ID=your-project-name
    ```
5. Set your project
    ```
    gcloud config set project $PROJECT_ID
    ```

6. Activate the project billing in the console

7. Authenticate if need it
    ```
    gcloud auth login
    ```
8. Enable needed services

    ```
    gcloud services enable run.googleapis.com cloudbuild.googleapis.com
    ```
9. Build the Image
    ```
    gcloud builds submit --tag gcr.io/$PROJECT_ID/fastapi-app
    ```
10. Deploy
    ```
    gcloud run deploy fastapi-app \
    --image gcr.io/$PROJECT_ID/fastapi-app \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated
    ```


11. Test get route
    ```
    curl https://your-cloud-run-url/
    ```

12. Test the post url

    ```
    curl -X POST https://fastapi-app-949091418184.us-central1.run.app/data \
    -H "Content-Type: application/json" \
    -H "x-api-key: your-secret-api-key" \
    -d '{"example": "data"}'
    ```
















