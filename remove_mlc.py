import sys
def check_comments(i,check_case,string):
	report_flag=0
	for j in range(i,i+len(check_case)):
		if(len(string)<j):
			return False
		if(string[j]==check_case[report_flag]):
			report_flag+=1
		else:
			return False
	if(report_flag==len(check_case)):
		return True
		
filename=sys.argv[1]
check_case=str(sys.argv[2])
end_case=str(sys.argv[3])
to_check=""
read_char=0
write_char=0
fp=open(filename,'r')
wp=open(filename+"_wmlc",'w')
wp1=open(filename+"_multi_line_com_report",'w')
string=fp.readline()
mlc_flag=0
while(string):
	k=0
	for i in range(len(string)):
		read_char+=1
		if(k):
			k-=1
		else:
			flag_raised=0
			if(mlc_flag==0):
				to_check=check_case
			else:	
				to_check=end_case
			if(check_comments(i,to_check,string)):
				mlc_flag=1-mlc_flag
				k=len(to_check)-1
				flag_raised=1
			if(flag_raised):
				wp1.write(to_check)
				if(to_check==end_case):
					wp1.write("\n")
			else:
				if(mlc_flag==0):	
					wp.write(string[i])
					write_char+=1
				else:
					if(string[i]!='\n'):
						wp1.write(string[i])
	string=fp.readline()
wp1.write("\n Total number of characters : "+str(read_char)+"\n")
wp1.write("Number of characters written back : "+str(write_char)+"\n")
if(read_char!=0):
	wp1.write("Percentage of removal : "+str(100-(float(write_char)*100/float(read_char)))+"\n")
fp.close()
wp.close()
wp1.close()

