DESTDIR ?= /usr/local/bin

install:
	@sudo cp hash.py $(DESTDIR)/buster
	@sudo chmod +x $(DESTDIR)/buster
	@echo "Installation Successful!"

uninstall:
	@sudo rm -f $(DESTDIR)/buster
	@echo "Hash-Buster has been removed"
