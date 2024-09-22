#!/usr/bin/env bash

#EXCLUDE="–exclude '*.log' –exclude '*.pyc'"


do_rsync() {
    sudo rsync -av --exclude *.log --exclude venv --progress . root@ubuntu.livenowhy.com::share/  --password-file=/etc/rsyncd.passwd
}

while true
do
    echo "sleep"
    do_rsync
    sleep 5
done
