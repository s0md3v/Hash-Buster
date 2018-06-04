#!/usr/bin/env python3
import requests
import argparse
import os
from re import search, findall
parser = argparse.ArgumentParser()
parser.add_argument('-s', help='hashed string', dest='hash')
parser.add_argument('-f', help='file containing hashes', dest='path')
parser.add_argument('-d', help='directory containing hashes', dest='dir')
args = parser.parse_args()

#Colors and shit like that
white = '\033[97m'
green = '\033[92m'
red = '\033[91m'
yellow = '\033[93m'
end = '\033[0m'
back = '\033[7;91m'
info = '\033[33m[!]\033[0m'
que = '\033[34m[?]\033[0m'
bad = '\033[31m[-]\033[0m'
good = '\033[32m[+]\033[0m'
run = '\033[97m[~]\033[0m'

def alpha(hashvalue):
    response = requests.get('https://lea.kz/api/hash/' + hashvalue).text
    match = search(r': "(.*?)"', response)
    if match:
        return match.group(1)
    else:
        if len(hashvalue) == 32:
            return beta(hashvalue)
        elif len(hashvalue) == 40:
            return delta(hashvalue)
        elif len(hashvalue) == 64:
            return theta(hashvalue)
        else:
            return False

def beta(hashvalue):
    data = {'md5' : hashvalue, 'x' : '21', 'y' : '8'}
    response = requests.post('http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php', data).text
    match = search(r'<span class=\'middle_title\'>Hashed string</span>: [^<]*</div>', response)    
    if match:
        return match.group(1)
    else:
        gamma(hashvalue)

def gamma(hashvalue):
    response = requests.get('http://www.nitrxgen.net/md5db/' + hashvalue).text
    if len(response) > 0:
        return response
    else:
        return False


def delta(hashvalue):
    data = {'auth':'8272hgt', 'hash':hashvalue, 'string':'','Submit':'Submit'}
    response = requests.post('http://hashcrack.com/index.php' , data).text
    match = search(r'<span class=hervorheb2>(.*?)</span></div></TD>', response)
    if match:
        return match.group(1)
    else:
        return False

def omega(hashvalue):
    data = {'hash':hashvalue, 'decrypt':'Decrypt'}
    response = requests.post('http://md5decrypt.net/en/Sha256/', data=data).text
    match = search (r'<b>(.*?)</b><br/><br/>', response)
    if match:
        return match.group(1)
    else:
        return False

def theta(hashvalue):
    response = requests.get('http://md5decrypt.net/Api/api.php?hash=%s&hash_type=sha256&email=deanna_abshire@proxymail.eu&code=1152464b80a61728' % hashvalue).text
    if len(response) != 0:
        return response
    else:
        return False

print ('''\033[1;97m_  _ ____ ____ _  _    ___  _  _ ____ ___ ____ ____ 
|__| |__| [__  |__|    |__] |  | [__   |  |___ |__/ 
|  | |  | ___] |  |    |__] |__| ___]  |  |___ |  \  %sv2.0\033[0m\n''' % red)

def crack(hashvalue):
    if len(hashvalue) == 32:
        if not args.path:
            print ('%s Hash function : MD5' % info)
        result = alpha(hashvalue)
        if result:
            return result
        else:
            return False
    elif len(hashvalue) == 40:
        if not args.path:
            print ('%s Hash function : SHA1' % info)
        result = alpha(hashvalue)
        if result:
            return result
        else:
            return False
    elif len(hashvalue) == 64:
        if not args.path:
            print ('%s Hash function : SHA-256' % info)
        result = alpha(hashvalue)
        if result:
            return result
        else:
            return False
    else:
        print ('%s This hash is not supported.' % bad)
        quit()

if args.dir:
    os.system('grep -Pr "[a-f0-9]{64}|[a-f0-9]{40}|[a-f0-9]{32}" %s --exclude=\*.{png,jpg,jpeg,mp3,mp4,zip,gz} | grep -Po "[a-f0-9]{64}|[a-f0-9]{40}|[a-f0-9]{32}" >> %s.txt' % (args.dir, args.dir.split('/')[-1]))

elif args.path:
    lines = []
    matches = set()
    result = {}
    with open(args.path, 'r') as f:
        for line in f:
            lines.append(line.strip('\n'))
    for line in lines:
        match = findall(r'[a-f0-9]{64}|[a-f0-9]{40}|[a-f0-9]{32}', line)
        if match:
            for h in match:
                matches.add(h)
    print ('%s Hashes found: %i' % (info, len(matches)))
    for hashvalue in matches:
        resp = crack(hashvalue)
        if resp:
            result[hashvalue] = resp
    with open('cracked-%s' % args.path.split('/')[-1], 'w+') as f:
        for hashvalue, cracked in result.items():
            f.write(hashvalue + ':' + cracked + '\n')
elif args.hash:
    result = crack(args.hash)
    if result:
        print (result)
    else:
        print ('%s Sorry this hash isn\'t present in our database.')
