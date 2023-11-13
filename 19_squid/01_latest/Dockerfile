FROM ubuntu/squid:latest
MAINTAINER livenowhy <livenowhy@hotmail.com>

RUN mkdir -p /data/cache
ADD squid_passwd /etc/squid/squid_passwd
ADD pass_squid.conf /etc/squid/squid.conf
