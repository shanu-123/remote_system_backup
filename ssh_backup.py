
# Remote System Network:
# Write a backup script to take backup of remote system config file(Create a temprory config folder with some files in it)
# (Install server on your pc and take ssh of your system(127.0.0.1) and take backup of files)

import paramiko
import time
import datetime
import os

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
timestamp = str(datetime.datetime.now().timestamp()).split(".")[0]

print("connecting...........")
ssh_client.connect(hostname="127.0.0.1",port=22,
		username="shanu",password="shanu") # connecting to remote pc

print("compressing....................")
stdin,stdout,stderr = ssh_client.exec_command("tar -cvf backup"+timestamp+".bz2 temp/\n") # compressing the file
print(stdout.read().decode())
time.sleep(2)

print("copying...........")
os.system("scp shanu@127.0.0.1:/home/shanu/networking/remote_system_network/backup.bz2 ~/backups1") # copying the file
