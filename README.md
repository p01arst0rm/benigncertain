# benigncertain
Simple exploit test for benigncertain (Equation Group's BENIGNCERTAIN tool - a remote exploit to extract Cisco VPN private keys) 
The port is based on the code from https://github.com/ross-bradley/benign-certain 

The script is meant to be used as quick verification for the case other methods include metasploit's module and a more extensive version can be found at:
https://github.com/3ndG4me/CVE-2016-6415-BenignCertain-Monitor

## Usage
```
for i in {1..30}; do python benign.py -n 1024 -o outfile -i intest 193.127.189.251  && echo "***RESPONSE***" && hexdump -C outfile  && echo "***REQUEST***" &&hexdump -C intest ; done
```

The response and request should contain different data 

## References

```
This generates a packet file which can be used as input to the binary bc-id, which sends the packet to the victim host. Hector Martin notes that it sends a IKE packets with a large Group-Prime option, and speculates that if the victim host is replying using the request length but only filling in the requested 768 bit prime, then it returns a buffer of uninitialised data following it.
https://github.com/musalbas/musalbas.com-old/blob/master/_posts/2016-08-18-equation-group-benigncertain.md
```
