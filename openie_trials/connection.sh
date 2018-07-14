#!/bin/bash

gcloud compute ssh sam --zone asia-south1-c



# To copy the local file "file-1" to "my-instance" in the "us-central1-a" zone, you can use:

# gcloud compute scp ~/file-1 my-instance:~/remote-destination --zone us-central1-a

# to copy from instance to local
# gcloud compute scp my-instance:~/file-1 ~/local-destination --zone us-central1-a