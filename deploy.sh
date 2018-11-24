gcloud container clusters create polls \
--scopes "https://www.googleapis.com/auth/userinfo.email","cloud-platform" \
--num-nodes 4 --zone "us-central1-a"

gcloud container clusters get-credentials polls --zone "us-central1-a"

kubectl create secret generic cloudsql-oauth-credentials --from-file=credentials.json=/home/ed/Downloads/ek-gke-django-test-66950c294553.json

kubectl create secret generic cloudsql --from-literal=username=polls-users --from-literal=password=973frustUm72RD%.leAd

kubectl create -f kubedeploy.yaml
