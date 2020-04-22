#EC2 Instance Setup

Once you've created an EC2 instance, these files will turn it into an automated Minecraft server upon startup.

##systemd service

The minecraft.service file will allow the minecraft server to start automatically when your EC2 instance is started.
Before using it, you must ensure you have java installed, and update these values for your server:

 - WorkingDirectory must be set to the ABSOLUTE path from which you wish to run the server.
 - ExecStart must be updated with the path to the server.jar file, and the min and max memory allocation updated for your requirements.

To use the minecraft.service file, place it into /etc/systemd/system/

Then, run the following commands (may have to run with sudo):

```
systemctl daemon-reload
systemctl start minecraft
systemctl enable minecraft
```

These three commands will refresh the daemon configs, start the minecraft server, and enable it, meaning the server will run when the EC2 instance is started.

##S3 backup on stopping instance

If you wish to save a simple backup of your world to S3 every time you stop the server, add the following to your service file, under [Service]:
 
```
TimeoutStopSec= 180
ExecStop=/home/user/folder/s3-backup.sh
``` 

s3-backup.sh is a script you can find in this folder - be sure to update the bucket name to match the S3 bucket you wish to use. The path to the script must be the absolute path or it gets ignored by systemd.
The timeout gives the instance 3 minutes to backup to S3 before systemd forces closure and reports a failure (When the backup is complete, the service will end, it won't wait three minutes)

After this, run these commands:

```
systemctl daemon-reload
systemctl stop minecraft
systemctl start minecraft
``` 

MAKE COMPLETELY SURE YOUR EC2 INSTANCE AND S3 BUCKET ARE IN THE SAME REGION OR YOU WILL BE CHARGED FOR DATA TRANSFER COSTS

You can then test out stopping the EC2 instance, and if your AWS authentication and permissions are correct you should get a folder called world appear in your specified bucket.
From now on, every time you stop the server you'll retain a copy of the world both before and after you play - just in case the world gets corrupted etc. whilst you're playing/after you've played.
If you wanted to go further you could enable versioning on the bucket, but you'd be storing a lot of data, and cheap is the order of the day around here.