#!/usr/bin/python
"""A simple code to calculate"""
# Filename:calc.py

import sys

if __name__=='__main__':
	command = sys.argv[1]
	nums = [float(a) for a in sys.argv[2:]]
	if command == 'add':
		print sum(nums)
	elif command == 'multiply':
		print reduce(lambda x, y: x * y,nums)
	else:
		print 'Command not found' 
