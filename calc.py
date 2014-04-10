"""A simple code to calculate"""
#!/usr/bin/python
# Filename:calc.py

#A=int(raw_input("Enter A:"))
#B=int(raw_input("Enter B:"))
#c = A + B 
#print c

# Now  we square C
#print c*c

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
	



# random comment
