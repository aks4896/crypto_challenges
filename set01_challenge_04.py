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

	return output

def ascii_score(str1, key,debug=0):
	score = 0
	for b in str1:
		decoded_byte = key ^ b
		
		if decoded_byte < ascii_low:
			#print("Rejected {}, key {}, byte: {}".format(decoded_byte,key,b))
			return 0;
		if decoded_byte > ascii_high:
			return 0;
		if decoded_byte in common_letter:
			score += 1;
			
	if debug:
		print("Key: {:3d}, Score: {}".format(key,score))
	return(score)

i = 0

with open('set01_challenge_04_data.txt','r') as f:
	for line in f:
		i += 1
		#print("Starting line {}, length: {}".format(i, len(line.strip())))
		raw1 = bytearray.fromhex(line.strip())

		length = len(raw1)

		score = []
		decoded = []
		high_key = 0
		next_high_key = 0


		for key in range(0,256):
			score.append(ascii_score(raw1, key,debug=0))
			
			if(score[key] > score[high_key]):
				print("key: {}".format(key))
				next_high_key = high_key
				high_key = key
			
			key_str = bytearray([key] * len(raw1))
			decoded.append(str_xor(raw1, key_str))
			if True:
				if key == 88:#score[key] != 0:
					print("Line: {:3d}, key: {:3d}, Score: {:2d}, len: {}, String: {}".format(i,key,score[key],len(decoded[key]),decoded[key]))
					print("len: {}, keystr: {}".format(len(key_str),key_str))
					print("Input String: {}".format(raw1))

		if score[high_key] != 0 and False:
			#print("Winner is: ")
			print("Line: {:3d}, key: {:3d}, Score: {:2d}, String: {}".format(i,high_key,score[high_key],decoded[high_key]))
		if score[next_high_key] != 0 and False:
			#print("Next Winner is: ")
			print("Line: {:3d}, key: {:3d}, Score: {:2d}, String: {}".format(i,next_high_key,score[next_high_key],decoded[next_high_key]))







