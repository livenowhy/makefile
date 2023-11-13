SUBDIRS=01_latest 02_base 03_ethnic 04_temporalio 05_3.6-alpine

subdirs:
	for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir; \
	done