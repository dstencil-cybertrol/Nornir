#!/bin/bash

pass=$(</home/user/nornir/nornir/.gitignore/creds.txt)


docker exec -it -w /root/nornir spe-nornir ./nornir_facts.py >> facts.txt
# git add .
# git commit -m "YYYY-MM-DD"
# git push 'http://docker:'$pass'@10.67.104.65:3000/administrator/nornir.git'
