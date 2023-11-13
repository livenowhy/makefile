SUBDIRS=01_alpine 02_python 03_centos 04_mongo 05_mysql 06_redis 07_rabbitmq 08_nas 09_node \
10_k8s 12_influxdb 13_golang 14_nginx 15_bytebase

subdirs:
	for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir; \
	done