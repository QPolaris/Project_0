#!/usr/bin/python3
#####################################################
#############  LEAVE CODE BELOW  ALONE  #############
# Include base directory into path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

# Import tester
from tester import failtest, passtest, assertequals, runcmd, preparefile, runcmdsafe
#############    END UNTOUCHABLE CODE   #############
#####################################################

###################################
# Write your testing script below #
###################################
python_bin = sys.executable
import pickle

# prepare necessary files
preparefile('./test.py')

# run test file
b_stdout, b_stderr, b_exitcode = runcmdsafe(f'{python_bin} ./test.py')


# convert stdout bytes to utf-8
stdout = ""
stderr = ""
answer = 0
try:
	stdout = b_stdout.decode('utf-8')
	stderr = b_stderr.decode('utf-8')
except:
	pass

# stdout check
try:
	with open('output', 'rb') as file1:
		answer = float(pickle.load(file1))
		runcmdsafe('rm ./output')
except ValueError:
	failtest(stdout+"\n\n"+stderr)
	exit()

if -5.01 < answer < -4.99:
	passtest('')
else:
	failtest(stdout+"\n\n"+stderr)
