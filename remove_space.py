import sys
import os
filename=sys.argv[1]
fp=open(filename,'r')
wp=open(filename+"_ws",'w')
string=fp.readline()
while(string):
	string=string.strip('\n')
	string=string.strip(' ')
	string=string.strip('\t')
	string=string.strip(' ')
	wp.write(string+"\n")
	string=fp.readline()
wp.close()
fp.close()
