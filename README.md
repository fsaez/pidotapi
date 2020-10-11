## Kubernetes
# Crear cluster K8s en GKE
export my_zone=us-central1-a
export my_cluster=falabella-cluster-1
source <(kubectl completion bash)
gcloud container clusters create $my_cluster \
   --num-nodes 3 --enable-ip-alias --zone $my_zone
gcloud container clusters get-credentials $my_cluster --zone $my_zone


# Github Actions
Github
- Repo
- Secrets

GKE
- Google Cloud service account  (https://console.cloud.google.com/iam-admin/serviceaccounts)
- Cloud IAM roles:
-- Kurnetes Engine Developer
-- Storage Admin
- Create a JSON service account key 

GKE_EMAIL 
github-actions@falabella-291504.iam.gserviceaccount.com

GKE_KEY
archivo json

GKE_PROJECT
falabella-291504




# Compilar imagen
git pull ..
cd backend
gcloud builds submit --config cloud-build.yml

# Deployment de imagen en K8s
web.yaml
kubectl create -f web.yaml --save-config
 kubectl get deployment
kubectl create -f web-lb.yaml
 kubectl get service web-lb
kubectl create -f web-ingress.yaml
 kubectl get ingress
kubectl create -f web-autoscaler.yaml
 kubectl get hpa

## Benchmark
python benchmark/bench.py -u http://34.70.71.49/pi/?random_limit=100 -w 1 -r 100