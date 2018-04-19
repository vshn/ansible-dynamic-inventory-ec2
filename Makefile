PYTHON_SITELIB_DIR ?= usr/lib/python2.7/site-packages

all:	#nothing to build

install:
	mkdir -p $(DESTDIR)/$(PYTHON_SITELIB_DIR)/ansible/contrib/inventory
	cp -v ec2.py $(DESTDIR)/$(PYTHON_SITELIB_DIR)/ansible/contrib/inventory
	chmod +x $(DESTDIR)/$(PYTHON_SITELIB_DIR)/ansible/contrib/inventory/ec2.py
	cp -v ec2.ini $(DESTDIR)/$(PYTHON_SITELIB_DIR)/ansible/contrib/inventory
