SUBDIRS=01_alertmanager 02_remote_storage_adapter 03_kapacitor 04_telegraf 05_pushgateway

subdirs:
	for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir; \
	done