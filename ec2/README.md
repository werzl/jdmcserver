The minecraft.service file will allow the minecraft server to start automatically when your EC2 instance is started.
Before using it, you must ensure you have java installed, and update these values for your server:

 - WorkingDirectory must be set to the ABSOLUTE path from which you wish to run the server.
 - ExecStart must be updated with the path to the server.jar file, and the min and max memory allocation updated for your requirements.

To use the minecraft.service file, place it into /etc/systemd/system

Then, run the following commands (may have to run with sudo):

```
systemctl daemon-reload
systemctl start minecraft
systemctl enable minecraft
```

These three commands will refresh the daemon configs, start the minecraft server, and enable it, meaning the server will run when the EC2 instance is started.