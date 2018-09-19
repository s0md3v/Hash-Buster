# Hash-Buster
Hash Buster is a program which uses several APIs to perform hash lookups.

![banner](https://image.ibb.co/nGNvso/Screenshot_from_2018_06_04_20_18_00.png)

## Features
- Automatic hash type identification
- Supports MD5, SHA1, SHA256, SHA384, SHA512
- Can extract & crack hashes from a file
- Can find hashes from a directory, recursively
- Multi-threading

## Insallation & Usage
Hash-Buster can be run directly from the python script but I highly suggest you to install it with the following command:

`make install`

After the installation, you will be able to access it with `buster` command.

#### Cracking a single hash
`buster -s <hash>`
#### Finding hashes from a directory
`buster -d /root/Documents`
#### Cracking hashes from a file
`buster -f /root/hashes.txt`
#### Specifiying number of threads
`buster -f /root/hashes.txt -t 10`

### As powerful as Hulk, as intelligent as Bruce Banner
#### Single Hash
You don't need to specify the hash type. Hash Buster will identify and *crack* it under 3 seconds.
#### Cracking hashes from a file
Hash Buster can find your hashes even if they are stored in a file like this
```
simple@gmail.com:21232f297a57a5a743894a0e4a801fc3
{"json@gmail.com":"d033e22ae348aeb5660fc2140aec35850c4da997"}
surrondedbytext8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918surrondedbytext
```
#### Finding hashes from a directory
Yep, just specify a directory and Hash Buster will go through all the files and directories present in it, looking for hashes.

### License
Hash-Buster is licensed under MIT License.
