#!/usr/bin/env bash

supervisord -c /etc/supervisord.conf

while true
do
    echo "sleep"
    sleep 60
done
