import sys
import os
filename=sys.argv[1]
fp=open(filename+"_sort",'r')
fp1=open(filename+"_st_sort",'r')
fp2=open(filename+"_result",'w')
f1=[]
f2=[]
string=fp.readline()
while(string):
	f1.append(string)
	string=fp.readline()
string=""
string=fp1.readline()
while(string):
	f2.append(string)
	string=fp1.readline()
l1=len(f1)
l2=len(f2)
if(l1<l2):
	length=l1
else:
	length=l2
total_char=0
wrong_char=0
i=0
while(i<len(f1) and i<len(f2)):
	s1=f1[i]
	s2=f2[i]
	q1=len(s1)
	q2=len(s2)
	i1=0
	i2=0
	t=0
	c=0
	flag=0
	while(i1<q1 and i2<q2):
		if(s1[i1]==s2[i2]):
			i1+=1
			i2+=1
			t+=1
		else:
			c+=1
			t+=1
			if(s1[i1]==' '):
				i1+=1
			elif(s2[i2]==' '):
				i2+=1
			else:
				if(s1[i1]<s2[i2]):
					f1.pop(i)
				else:
					f2.pop(i)
				i-=1
				length-=1
				flag=1
				break
	if(flag==0):
		if(i1!=q1):
			wrong_char+=q1-i1
			total_char+=q1-i1
		if(i2!=q2):
			wrong_char+=q2-i2
			total_char+=q1-i2
		total_char+=t
		wrong_char+=c
	i+=1
fp2.write(str(float((total_char-wrong_char)*100/total_char)))
print("total module done")
