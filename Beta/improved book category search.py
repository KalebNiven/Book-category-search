import pandas as pd
import re
import string

csv_file = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Overdrive\\all_3_lists.csv"
df = pd.read_csv(csv_file)
#C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Overdrive
reg1 = r"/.*$"
#book list 1 = Philosophy
#book list 2 = Psychology
#book list 3 = Computer Technology

book1_titles = df.Philosophy_title
book1_links = df.Philosophy_link
book1_id_sorted = [[]]
book1_titles_sorted = [[]]
book2_titles = df.Psychology_title
book2_links = df.Psychology_link
book2_id_sorted = [[]]
book2_titles_sorted = [[]]
book3_titles = df.Computer_Technology_title
book3_links = df.Computer_Technology_link

for i,x in enumerate(book1_links):
    try:
        x = x.replace("https://www.overdrive.com/media/","")
        x = re.sub(reg1,"",x)
        book1_links[i] = x
    except AttributeError:
        continue

for i,x in enumerate(book2_links):
    try:
        x = x.replace("https://www.overdrive.com/media/","")
        x = re.sub(reg1,"",x)
        book2_links[i] = x
    except AttributeError:
        continue

for i,x in enumerate(book3_links):
    try:
        x = x.replace("https://www.overdrive.com/media/","")
        x = re.sub(reg1,"",x)
        book3_links[i] = x
    except AttributeError:
        continue

while len(book1_id_sorted) <= 9:
    book1_id_sorted.append([])
    book2_id_sorted.append([])
    # book1_titles_sorted.append([])

for i,x in enumerate(book1_links):
    try:
        if x[0].isdigit():
            book1_id_sorted[int(x[0])].append(x)
            # book1_titles_sorted[int(x[0])].append(book1_titles[i])
    except TypeError:
        continue

for i,x in enumerate(book2_links):
    try:
        if x[0].isdigit():
            book2_id_sorted[int(x[0])].append(x)
            # book1_titles_sorted[int(x[0])].append(book1_titles[i])
    except TypeError:
        continue

    # print (z)
print("Working..")
for i,x in enumerate(book3_links):
    if x in book1_id_sorted[int(x[0])]:
        print (book3_titles[i]+"\t"+"https://www.overdrive.com/media/"+x)
