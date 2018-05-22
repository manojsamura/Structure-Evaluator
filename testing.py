import pathlib
import os
import datetime

now=datetime.datetime.now()
print(now)

p=pathlib.Path("Submissions1/")
a=list(p.glob('*'))
count=-1
for i in a:
	print(i)
	count+=1
	os.system("clear")
	print("Students Done :"+str(count)+"\n\n\n")
	print(i)
	k=str(i)
	p1=pathlib.Path(str(i)+"/")
	b=list(p1.glob("*.c"))
	for j in b:
		s_id=str(j).split('/')
		s_id=s_id[len(s_id)-1]
		print(str(j))
		os.system("python /home/manoj/system/structuring/run_module.py "+str(j)+" ")
		os.system("cat "+str(j)+"_result ")

now1=datetime.datetime.now()
print(now1)
print(now1-now)
