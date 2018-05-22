import sys
import os
filename=sys.argv[1]
os.system("python /home/manoj/system/structuring/remove_bracket.py "+filename)
os.system("python /home/manoj/system/structuring/remove_mlc.py "+filename+"_wb \'/*\' \'*/\'")
os.system("python /home/manoj/system/structuring/remove_slc.py "+filename+"_wb_wmlc \'//\'")
os.system("python /home/manoj/system/structuring/remove_space.py "+filename+"_wb_wmlc_wslc")
os.system("python /home/manoj/system/structuring/remove_el.py "+filename+"_wb_wmlc_wslc_ws")
os.system("mv "+filename+"_wb_wmlc_wslc_ws_wel "+filename+"_cr")
os.system("rm "+filename+"_w*")
