# Fastapi CI/CD Demo

利用 GitHub Action 實現 CI / CD 自動部署 Fastapi 至 GKE

### 環境

- Dokcer
- Python 3.7.7
- Fastapi

### Fastapi 本機測試及開發

```shell
$ docker build -t fastapi-cicd-demo:latest .

$ docker run --rm -p 8000:8000 fastapi-cicd-demo:latest
```

### Google Cloud Platform project & service account 設定

1. 建立 Service Account 並下載 key json

   ```
   Role 選擇
   Kubernetes Engine > Kubernetes Engine Developer
   Cloud Storage > Storage Admin
   ```

2. 將 service_account.json 內容複製出來並填入 GitHub secrets

3. 將 GCP project id 填入 secrets

![GitHub Secrets](/docs/github_secrets.png)

### 部署到 Kubernetes Engine (GKE)

1. 安裝及設定 [Google Cloud SDK (gcloud)](https://cloud.google.com/sdk/docs/install)

2. 建立 GKE cluster

   ```shell
   $ gcloud container clusters create fastapi-cicd-cluster \
   --zone asia-east1-b \
   --num-nodes=1
   ```

3. 查詢是否建立成功

   ```shell
   $ gcloud compute instances list
   ```

4. 建立一個 git tag

   ```shell
   # get commit log
   $ git log --oneline

   # git tag on commit
   $ git tag {tag_name} {commit_id}
   ```

5. Push tag to trigger GitHub Action

   ```shell
   $ git push origin {tag_name}
   ```

6. 檢查 GitHub Action build & deploy 結果

7. GKE 狀態查詢
   ```shell
   $ kubectl get all
   ```
   ![GitHub Secrets](/docs/result_kubectl_get_all.png)

### Reference
  - https://cloud.google.com/gcp/getting-started/?hl=zh-TW
  - https://cloud.google.com/kubernetes-engine
  - https://docs.github.com/en/free-pro-team@latest/actions
  - https://fastapi.tiangolo.com/
  - https://docs.docker.com/
