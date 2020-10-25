!/bin/bash
#This script will sync your world with an S3 bucket whenever the world is stopped. Make sure to update the values.
aws s3 sync /path/to/world/directory/ s3://bucket-name