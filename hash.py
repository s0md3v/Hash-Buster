#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#

import sys
from urllib import *

from re import search, findall

__author__  = "UltimateHackers"
__version__ = "0.0.3"

def banner():
	print((56 * '\033[31m-\033[1;m'))
	print "\t\033[97m     Made with \033[1;m\033[1;31m<3\033[1;31m\033[97m By Team Ultimate\033[1;m"
	print """\033[1;97m_  _ ____ ____ _  _    ___  _  _ ____ ___ ____ ____ 
|__| |__| [__  |__|    |__] |  | [__   |  |___ |__/ 
|  | |  | ___] |  |    |__] |__| ___]  |  |___ |  \  v1.0\033[1;m"""
	print "\033[1;32mServers Loaded: Alpha, Beta, Gamma, Delta, Omega, Lambda\033[1;m"
	print((56 * '\033[31m-\033[1;m'))

def usage():
	print """
Usage:
-------------------
	$ python2 hash.py -h/--hash HASH
	---
	$ python2 hash.py --hash 098f6bcd4621d373cade4e832627b4f6
	"""
	sys.exit()

def Omega(hash):
    data = urlencode({"hash":hash, "decrypt":"Decrypt"})
    html = urlopen("http://md5decrypt.net/en/Sha256/", data).read()
    match = search (r'<b>[^<]*</b><br/><br/>', html)

    if match:
        return match.group().split('<b>')[1][:-14]
    else:
    	return False

def Lambda(hash):
    data = urlencode({"hash":hash})
    html = urlopen("http://performancetesting.in/sha256decryption.php", data)
    match = search (r'Decrypted Text : </b>[^<]*</div>', html.read())

    if match:
        return match.group().split('</b>')[1][:-6]
    else:
    	return False

def Beta(hash):
    data = urlencode({"auth":"8272hgt", "hash":hash, "string":"","Submit":"Submit"})
    html = urlopen("http://hashcrack.com/index.php" , data).read()
    match = search (r'<span class=hervorheb2>[^<]*</span></div></TD>', html)

    if match:
        return match.group().split('hervorheb2>')[1][:-18]
    else:
    	return False

def Gamma(hash):
    purl = urlopen("http://www.nitrxgen.net/md5db/" + hash).read()

    if len(purl) > 0:
        return purl
    else:
    	return False

def Delta(hash):
	data = urlencode({"md5":hash,"x":"21","y":"8"})
	html = urlopen("http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php", data).read()
	match = search (r"<span class='middle_title'>Hashed string</span>: [^<]*</div>", find)

	if match:
	    return match.group().split('span')[2][3:-6]
	else:
		return False

def Alpha(hash):
    data = urlencode({"hash":hash,"submit":"Decrypt It!"})
    html = urlopen("http://md5decryption.com", data).read()
    match = search(r"Decrypted Text: </b>[^<]*</font>", html)

    if match:
        return match.group().split('b>')[1][:-7]
    else:
    	return False

def detectHash(hash):
	if len(hash) == 32:
		return "md5"

	elif len(hash) == 40:
		return "sha1"

	elif len(hash) == 64:
		return "sha-256"

	else:
		return None

def main(hash):
	hashType = detectHash(hash)

	if hashType != None:
		print "\033[1;33m[!]\033[1;m Hash function : %s"%(hashType.upper())

		if hashType == "sha1":
			site = "Beta" # ^^

			result = eval(site)(hash)

			if result != False:
				pass

		elif hashType == "sha256":
			site = "Lambda" #

			result = eval(site)(hash)

			if result != False:
				pass

		elif hashType == "md5":
			for site in ["Alpha", "Delta", "Gamma", "Beta", "Omega"]:
				result = eval(site)(hash) # ^^

				if result != False:
					break

		if result != False:
			print "\n\033[1;32m[+] Hash cracked by %s:\033[1;m"%(site), result

	else:
		print "\033[1;31m[-]\033[1;m This hash is not supported."

if __name__ == '__main__':
	banner()

	if len(sys.argv) == 3:
		if sys.argv[1] in ['-h', '--hash']:
			main(sys.argv[-1])
		else:
			usage()
	else:
		usage()