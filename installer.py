#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#

__author__ = "blackvkng"

import os, urllib2

def main():
	code = urllib2.urlopen('https://raw.githubusercontent.com/UltimateHackers/Hash-Buster/master/hash.py').read()

	file = open("/usr/bin/hash-buster", "w")
	file.write(code)
	file.close()
	
	os.system("chmod +x /usr/bin/hash-buster")

	print "[*] Installation finished, type 'hash-buster' to use program!"

if __name__ == "__main__":
	if os.name != "nt":
		if os.getuid() == 0:
			main()
		else:
			print "[-] Run as root!"
	else:
		print "[-] Just on Linux"
