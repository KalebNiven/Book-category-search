import pandas as pd
import re
import string
import csv


csv_file = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Overdrive\\Beta\\all_3_lists2.csv"
df = pd.read_csv(csv_file)
book1_title_output = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Overdrive\\Beta\\book1_title_output.txt"
book1_link_output = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Overdrive\\Beta\\book1_link_output.txt"

book2_title_output = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Overdrive\\Beta\\book2_title_output.txt"
book2_link_output = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Overdrive\\Beta\\book2_link_output.txt"

book1_titles = df.Psychology_title
book1_links = df.Psychology_link

book2_titles = df.Self_Improvement_title
book2_links = df.Self_Improvement_link

index = []
index2 = []

with open (book1_title_output,'w') as o:
    for i,x in enumerate(book1_titles):
        try:
            o.write(x)
            o.write("\n")
            index.append(i)
        except UnicodeEncodeError:
            continue
        except TypeError:
            print (x)
o.close()

with open (book1_link_output,'w') as o:
    for x in index:
        try:
            o.write(book1_links[x])
            o.write("\n")
        except UnicodeEncodeError:
            print (i)
o.close()

with open (book2_title_output,'w') as o:
    for i,x in enumerate(book2_titles):
        try:
            o.write(x)
            o.write("\n")
            index2.append(i)
        except UnicodeEncodeError:
            continue
        except TypeError:
            continue
o.close()

with open (book2_link_output,'w') as o:
    for x in index2:
        try:
            o.write(book2_links[x])
            o.write("\n")
        except UnicodeEncodeError:
            print (i)
o.close()
