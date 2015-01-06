import os
import sys

if os.path.isfile(os.getcwd()+"/TODOloc"):
	if os.path.getsize(os.getcwd()+"/TODOloc") == 0:
		print "no todo list location set, please provide file path"
		data = sys.stdin.readline()
		f = open(os.getcwd()+"/TODOloc",'w')
		f.write(data)
else:
	print "internal file corruption, exiting now"
	sys.exit()

f_= open(os.getcwd()+"/TODOloc",'r')
path = f_.readline()
f = open(''.join(path).rstrip('\n'), 'r')
for i in f:
	print i.rstrip('\n')
sys.exit()



