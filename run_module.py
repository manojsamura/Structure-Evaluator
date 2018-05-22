import sys
import os
filename=sys.argv[1]
os.system("cp "+filename+" "+filename+"_st")
os.system("indent "+filename+"_st")
os.system("python /home/manoj/system/structuring/code_cleaner.py "+filename)
os.system("python /home/manoj/system/structuring/code_cleaner.py "+filename+"_st")
print("code cleaner done")
os.system("sort -i "+filename+"_cr > "+filename+"_sort")
os.system("sort -i "+filename+"_st_cr > "+filename+"_st_sort")
print("Sorting done")
os.system("python /home/manoj/system/structuring/check_struct.py "+filename)
