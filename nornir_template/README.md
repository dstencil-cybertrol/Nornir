# Nornir Automation Framework


## Docker Method
```
$ cd /path/to/repo
$ docker build . -t nornir_v.01
$ docker run --name site-nornir nornir_v.01
### Check if application is running in docker

```
$ docker ps
CONTAINER ID   IMAGE                      COMMAND                  CREATED          STATUS          NAMES                       PORTS                                                                                    
fd6930df22d6   dstencil/ce:nornir_v.01    "python3"                30 minutes ago   Up 30 minutes   site-nornir

```

### Enter Folder with repo already cloned                                                                                        
```
$ cd nornir/nornir
```
### Run backup_configs.py and git add, commit, and push
``` 
$ ./switch_backup.sh

^^^^ END CREATING BACKUP ARCHIVE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[main 4c04fd1] YYYY-MM-DD
 4 files changed, 4 insertions(+)
Enumerating objects: 13, done.
Counting objects: 1920% (13/13), done.
Delta compression using up to 2 threads
Compressing objects: 1920% (5/5), done.
Writing objects: 1920% (7/7), 612 bytes | 612.00 KiB/s, done.
Total 7 (delta 6), reused 2 (delta 2)
remote: . Processing 1 references
remote: Processed 1 references in total
To "http://192.168.10.65:3000/administrator/nornir.git"
   3eebfa2..4c04fd1  main -> main
```
