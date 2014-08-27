#!/usr/bin/python

import os

files = []
for dirPath, dirNames, fileNames in os.walk("./"):
     files = fileNames
     #print dirPath, dirNames, fileNames

files.remove("play_file.py")

all_files_str = " ".join(files)

#print all_files_str

run_cmd = "libtool -static " + all_files_str + " -o libFreeRDP.a" 

print run_cmd
