#!/bin/bash

cd /home/user/nornir/nornir

pass=$(</home/user/nornir/nornir/.gitignore/creds.txt)
DATE=$(date +"%Y-%m-%d")
git pull 'http://docker:'$pass'@192.168.1.10:3000/administrator/nornir.git'



docker exec -it -w /root/nornir spe-nornir ./backup_configs.py
git add .
git commit -m $DATE
git push 'http://docker:'$pass'@192.168.1.10:3000/administrator/nornir.git'
