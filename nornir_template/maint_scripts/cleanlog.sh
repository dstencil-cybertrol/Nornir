#!/bin/bash

cd /home/user/nornir/nornir

pass=$(</home/user/nornir/nornir/.gitignore/creds.txt)
DATE=$(date +"%Y-%m-%d")


rm /home/user/nornir/nornir/nornir.log


touch /home/user/nornir/nornir/nornir.log

git add .

git commit -m "refreshed log: $DATE"
git push 'http://docker:'$pass'@192.168.10.65:3000/administrator/nornir.git'


echo "finished cleaning log"
