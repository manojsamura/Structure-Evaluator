import sys
filename=sys.argv[1]
fp=open(filename,'r')
wp=open(filename+"_wel",'w')
rp=open(filename+"_remove_el_report",'w')
string=fp.readline()
read_line=0
write_line=0
while(string):
	read_line+=1
	for i in string:
		if(i!='\n' and i!=' ' and i!='\t'):
			wp.write(string)
			write_line+=1
			break
	string=fp.readline()
rp.write("Total number of lines : "+str(read_line)+"\n")
rp.write("Number of lines : written back : "+str(write_line)+"\n")
rp.write("Percentage of Removal : "+str(100-(float(write_line)*100/float(read_line)))+"\n")
fp.close()
wp.close()
rp.close()	
