#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 16:55:10 2018

@author: Soe Than
"""

def add_to_list(scheduleObj):
    if line_count % 2 != 0:
        tag_line = "<tr bgcolor='DDEBF7'>"
    else:
        tag_line = "<tr>"
    for item in scheduleObj:
        tag_line = tag_line + "<td>" + item + "</td>"
    tag_line = tag_line + "</tr>\n" 
    html_tags.append(tag_line)
    if "Office Hour" in scheduleObj[3]:
        tag_line = "<tr bgcolor=\"#CCCCCC\" style=\"line-height:5px\"><td colspan=\""+str(len(scheduleObj))+"\">&nbsp;</td></tr>"
        html_tags.append(tag_line)
    #print(html_tags)
        
def writeOutSchedule(dis):
    outfile = open(dis+".html", "w+")
    for item in html_tags:
        outfile.writelines(item)
    del html_tags[:]
    outfile.close()
    

file = open("schedule.csv", "r")
"""discard the titles for now
"""
file.readline()
crs_count = 0
line_count = 0
html_tags = []
while True:
    line = file.readline()
    line_count = line_count + 1
    if line == "":
        break
    #print(line)
    line = line.strip()
    scheduleObj = line.split(";")
    #print(scheduleObj)
    if line_count == 1:
        dis = scheduleObj[0]
        add_to_list(scheduleObj)
    else:
        #does not work if it contains whitespace
        #fix later
        if dis not in scheduleObj[0]:
            writeOutSchedule(dis)
            dis = scheduleObj[0]
            
        add_to_list(scheduleObj)
            
file.close()        
    
        