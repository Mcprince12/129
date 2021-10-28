import csv 
import pandas as pd
data1=[]
data2=[]
with open("dwarf_star.csv","r")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data1.append(row)

with open("bright_stars.csv","r")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data2.append(row)

headers1=data1[0]
star_data1=data1[1:]
headers2=data2[0]
star_data2=data2[1:]

headers=headers1+headers2
star_data=[]
for i in star_data1:
    star_data.append(i)

for a in star_data2:
    star_data.append(a)

for headers, star_data in enumerate(star_data1):
    star_data.append(star_data1[headers]+star_data2[headers])

with open("final.csv","a+")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)