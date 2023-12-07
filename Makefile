SUBDIRS= 06_centos

subdirs:
	for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir; \
	done