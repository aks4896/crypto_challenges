#!/usr/bin/env python3

'''
Challenge URL: https://cryptopals.com/sets/1/challenges/2


'''
import base64
import binascii


def str_xor(str1, str2, debug=0):
	# sanity checks
	if len(str1) != len(str2):
		print("String lengths don't match, len(str1)={}, len(str2)={}".format(len(str1),len(str2)))

	output = bytearray(b"")

	print(output)

	for i in range(len(str1)):
		output.append(str1[i] ^ str2[i])
	
	if debug:
		print(output)
	return output


input_str1 = '1c0111001f010100061a024b53535009181c'

input_str2 = '686974207468652062756c6c277320657965'

raw1 = bytearray.fromhex(input_str1)

raw2 = bytearray.fromhex(input_str2)

print("Input string 1: {}".format(raw1))
print("Input string 2: {}".format(raw2))

xor = str_xor(raw1, raw2)

print("XOR of 1 and 2: {}".format(xor))

print("XOR of 1 and 2: {}".format(binascii.hexlify(xor)))
