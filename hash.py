#!/usr/bin/env python3

import re
import os
import requests
import argparse
import concurrent.futures
import json
from urllib.parse import quote
from requests.exceptions import RequestException
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

parser = argparse.ArgumentParser()
parser.add_argument('-s', help='hash', dest='hash')
parser.add_argument('-f', help='file containing hashes', dest='file')
parser.add_argument('-d', help='directory containing hashes', dest='dir')
parser.add_argument('-t', help='number of threads', dest='threads', type=int)
args = parser.parse_args()

#Colors and shit like that
end = '\033[0m'
red = '\033[91m'
green = '\033[92m'
white = '\033[97m'
dgreen = '\033[32m'
yellow = '\033[93m'
back = '\033[7;91m'
run = '\033[97m[~]\033[0m'
que = '\033[94m[?]\033[0m'
bad = '\033[91m[-]\033[0m'
info = '\033[93m[!]\033[0m'
good = '\033[92m[+]\033[0m'

cwd = os.getcwd()
directory = args.dir
file = args.file
thread_count = args.threads or 4
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
retries = 2
timeout = 20

if directory:
    if directory[-1] == '/':
        directory = directory[:-1]

def alpha(hashvalue, hashtype):
    url = u"http://md5.tellyou.top/MD5Service.asmx/HelloMd5"
    retries_count = 0
    while True:
        try:
            params = {u"Ciphertext": hashvalue}
            headers = dict(header, **{u"X-Forwarded-For": u"192.168.1.1"})
            req = requests.get(url, params=params, headers=headers, timeout=timeout)
            result = re.findall(r'<string xmlns="http://tempuri.org/">(.*?)</string>', req.text)
            if result:
                return result[0]
            else:
                return False
        except RequestException:
            retries_count += 1
            if retries_count >= retries:
                return False
        except:
            return False

def beta(hashvalue, hashtype):
    url = u"https://www.chamd5.org/"
    retries_count = 0
    while True:
        try:
            s = requests.Session()
            headers = dict(header, **{u"Content-Type": u"application/json", u"Referer": url,
                                              u"X-Requested-With": u"XMLHttpRequest"})
            data = {u"email": u"jxtepz93152@chacuo.net", u"pass": u"!Z3jFqDKy8r6v4", u"type": u"login"}
            s.post(u"{0}HttpProxyAccess.aspx/ajax_login".format(url), headers=headers, data=json.dumps(data),
                   timeout=timeout, verify=False)

            data = {u"hash": hashvalue, u"type": hashtype}
            req = s.post(u"{0}HttpProxyAccess.aspx/ajax_me1ody".format(url), headers=headers, data=json.dumps(data),
                         timeout=timeout, verify=False)
            rsp = req.json()
            msg = re.sub(r"<.+?>", u"", json.loads(rsp[u"d"])[u"msg"])
            if msg.find(u"\u7834\u89e3\u6210\u529f") > 0:
                plain = re.findall(r"\u660e\u6587:(.+?)\u6570\u636e\u6765\u6e90", msg)[0].strip()
                return plain
            elif msg.find(u"\u91d1\u5e01\u4e0d\u8db3") >= 0:
                return msg
            else:
                return False
        except RequestException:
            retries_count += 1
            if retries_count >= retries:
                return False
        except:
            return False

def gamma(hashvalue, hashtype):
    url = u"https://md5.gromweb.com/"
    retries_count = 0
    while True:
        try:
            params = {u"md5": hashvalue}
            req = requests.get(url, headers=header, params=params, timeout=timeout, verify=False)
            rsp = req.text
            if rsp.find(u"succesfully reversed") > 0:
                plain = re.findall(r'<em class="long-content string">(.*?)</em>', rsp)[0]
                return plain
            else:
                return False
            break
        except RequestException:
            retries_count += 1
            if retries_count >= retries:
                return False
        except:
            return False

def delta(hashvalue, hashtype):
    url = u"http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php"
    retries_count = 0
    while True:
        try:
            data = {u"md5": hashvalue}
            req = requests.post(url, headers=header, data=data, timeout=timeout)
            result = re.findall(r"Hashed string</span>:\s(.+?)</div>", req.text)
            if result:
                return result[0]
            else:
                return False
        except RequestException:
            retries_count += 1
            if retries_count >= retries:
                return False
                # break

def theta(hashvalue, hashtype):
    url = u"https://hashtoolkit.com/reverse-hash/"
    retries_count = 0
    while True:
        try:
            params = {u"hash": hashvalue}
            req = requests.get(url, headers=header, params=params, timeout=timeout, verify=False)
            rsp = req.text
            if rsp.find(u"No hashes found for") > 0:
                return False
            else:
                plain = re.findall(r'<a href="/generate-hash/\?text=(.*?)"', rsp, re.S)[0]
                return quote(plain)
        except RequestException:
            retries_count += 1
            if retries_count >= retries:
                return False
                # break
        except:
            return False
            # break

print ('''\033[1;97m_  _ ____ ____ _  _    ___  _  _ ____ ___ ____ ____
|__| |__| [__  |__|    |__] |  | [__   |  |___ |__/
|  | |  | ___] |  |    |__] |__| ___]  |  |___ |  \  %sv3.0\033[0m\n''' % red)

md5 = [gamma, alpha, beta, delta]#theta, delta]
sha1 = [beta, theta]
sha256 = [beta, theta]
sha384 = [beta, theta]
sha512 = [beta, theta]

def crack(hashvalue):
    result = False
    if len(hashvalue) == 32:
        if not file:
            print ('%s Hash function : MD5' % info)
        for api in md5:
            r = api(hashvalue, 'md5')
            if r:
                return r
    elif len(hashvalue) == 40:
        if not file:
            print ('%s Hash function : SHA1' % info)
        for api in sha1:
            r = api(hashvalue, 'sha1')
            if r:
                return r
    elif len(hashvalue) == 64:
        if not file:
            print ('%s Hash function : SHA-256' % info)
        for api in sha256:
            r = api(hashvalue, 'sha256')
            if r:
                return r
    elif len(hashvalue) == 96:
        if not file:
            print ('%s Hash function : SHA-384' % info)
        for api in sha384:
            r = api(hashvalue, 'sha384')
            if r:
                return r
    elif len(hashvalue) == 128:
        if not file:
            print ('%s Hash function : SHA-512' % info)
        for api in sha512:
            r = api(hashvalue, 'sha512')
            if r:
                return r
    else:
        if not file:
            print ('%s This hash type is not supported.' % bad)
            quit()
        else:
            return False

result = {}

def threaded(hashvalue):
    resp = crack(hashvalue)
    if resp:
        print (hashvalue + ' : ' + resp)
        result[hashvalue] = resp

def grepper(directory):
    os.system('''grep -Pr "[a-f0-9]{128}|[a-f0-9]{96}|[a-f0-9]{64}|[a-f0-9]{40}|[a-f0-9]{32}" %s --exclude=\*.{png,jpg,jpeg,mp3,mp4,zip,gz} |
        grep -Po "[a-f0-9]{128}|[a-f0-9]{96}|[a-f0-9]{64}|[a-f0-9]{40}|[a-f0-9]{32}" >> %s/%s.txt''' % (directory, cwd, directory.split('/')[-1]))
    print ('%s Results saved in %s.txt' % (info, directory.split('/')[-1]))

def miner(file):
    lines = []
    found = set()
    with open(file, 'r') as f:
        for line in f:
            lines.append(line.strip('\n'))
    for line in lines:
        matches = re.findall(r'[a-f0-9]{128}|[a-f0-9]{96}|[a-f0-9]{64}|[a-f0-9]{40}|[a-f0-9]{32}', line)
        if matches:
            for match in matches:
                found.add(match)
    print ('%s Hashes found: %i' % (info, len(found)))
    threadpool = concurrent.futures.ThreadPoolExecutor(max_workers=thread_count)
    futures = (threadpool.submit(threaded, hashvalue) for hashvalue in found)
    for i, _ in enumerate(concurrent.futures.as_completed(futures)):
        if i + 1 == len(found) or (i + 1) % thread_count == 0:
            print('%s Progress: %i/%i' % (info, i + 1, len(found)), end='\r')

def single(args):
    result = crack(args.hash)
    if result:
        print (f"Hash found: %s{result}." % good)
    else:
        print ('%s Hash was not found in any database.' % bad)

if directory:
    try:
        grepper(directory)
    except KeyboardInterrupt:
        pass

elif file:
    try:
        miner(file)
    except KeyboardInterrupt:
        pass
    with open('cracked-%s' % file.split('/')[-1], 'w+') as f:
        for hashvalue, cracked in result.items():
            f.write(hashvalue + ':' + cracked + '\n')
    print ('%s Results saved in cracked-%s' % (info, file.split('/')[-1]))

elif args.hash:
    single(args)
