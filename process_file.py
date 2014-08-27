#!/usr/bin/python

f = open("./all_libs.txt", 'r')

line_arr = []

for line in f:
     if "armv7" in line:
          if "armv7s" in line:
               pass
          else:
               line = line.strip()
               line_arr.append(line)

combine_str = " ".join(line_arr)

run_cmd = "cp " + combine_str + " ./KENNY_TEMP/all_arm7_libs"

print run_cmd

