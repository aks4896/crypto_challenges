#!/usr/bin/env python3

'''
Challenge URL: https://cryptopals.com/sets/1/challenges/3


'''
import base64
import binascii

DEBUG = 0;

ascii_low = b" "[0]
ascii_high = b"~"[0]
common_letter = b"etaoinshETAOINSH "

def str_xor(str1, str2, debug=0):
	# sanity checks
	if len(str1) != len(str2):
		print("String lengths don't match, len(str1)={}, len(str2)={}".format(len(str1),len(str2)))

	output = bytearray(b"")

	for i in range(len(str1)):
		output.append(str1[i] ^ str2[i])
	
	if debug:
		print(output)
	return output

def ascii_score(str1, key,debug=0):
	score = 0
	for b in str1:
		decoded_byte = key ^ b
		
		if decoded_byte < ascii_low:
			return 0;
		if decoded_byte > ascii_high:
			return 0;
		if decoded_byte in common_letter:
			score += 1;
			
	if debug:
		print("Key: {}, Score: {}".format(key,score))
	return(score)


input_str1 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

raw1 = bytearray.fromhex(input_str1)
length = len(raw1)

score = []
decoded = []
high_key = 0


for key in range(0,256):
	score.append(ascii_score(raw1, key,debug=DEBUG))
	
	if(score[key] > score[high_key]):
		high_key = key
	
	key_str = bytearray([key] * len(raw1))
	decoded.append(str_xor(raw1, key_str))
	if DEBUG:
		print("key: {}, Score: {}, String: {}".format(key,score[key],decoded[key]))

print("Winner is: ")

print("key: {}, Score: {}, String: {}".format(high_key,score[high_key],decoded[high_key]))







