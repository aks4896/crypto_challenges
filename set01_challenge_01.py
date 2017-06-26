#!/usr/bin/env python3

'''
Challenge URL: https://cryptopals.com/sets/1/challenges/1


'''
import base64
import binascii


input_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

raw = bytearray.fromhex(input_str)

print("Input hex: {}".format(input_str))

print("Raw data: {}".format(raw))

print("Base64 Encode: {}".format(base64.b64encode(raw)))
