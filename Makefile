SUBDIRS= 07_rabbitmq 08_nas 09_node \
10_k8s 12_influxdb 13_golang 14_nginx 15_bytebase

subdirs:
	for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir; \
	done