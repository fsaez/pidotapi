## Kubernetes

export my_zone=us-central1-a
export my_cluster=falabella-cluster-1
source <(kubectl completion bash)
gcloud container clusters create $my_cluster \
   --num-nodes 3 --enable-ip-alias --zone $my_zone
gcloud container clusters get-credentials $my_cluster --zone $my_zone

web.yaml
kubectl create -f web.yaml --save-config
 kubectl get deployment
kubectl create -f web-lb.yaml
 kubectl get service web-lb
kubectl create -f web-ingress.yaml
 kubectl get ingress
kubectl create -f web-autoscaler.yaml
 kubectl get hpa