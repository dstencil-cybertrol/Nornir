# Crontabs Setup on Host
```
0 0 1 * * /home/user/nornir/nornir/switch_backup.sh
sudo 0 0 1 * * /home/user/nornir/nornir/maint_scripts/cleanlog.sh
0 0 14 * * /home/user/nornir/nornir/switch_backup.sh
0 0 1 * * /home/user/nornir/nornir/maint_scripts/clean_config-archive.sh
```