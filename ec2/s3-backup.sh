#!/bin/bash
#This script will take your world files and upload them to a specified S3 bucket.
#Requires AWS CLI and bucket permissions (would recommend using an IAM role)
#Any previous backup will be moved to the subdirectory "old" to give a copy of the world before and after starting the server.
aws s3 mv s3://BUCKET-NAME/world s3://BUCKET-NAME/old --recursive
aws s3 cp path/to/world/folder/ s3://BUCKET-NAME/world --recursive