import sys
import os
filename=sys.argv[1]
fp=open(filename,'r')
wp=open(filename+"_wb",'w')
char=fp.read(1)
while(char):
	if(char=='}' or char=='{'):
		wp.write('\n')
	else:
		wp.write(char)
	char=fp.read(1)
fp.close()
wp.close()
