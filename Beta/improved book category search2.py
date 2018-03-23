import pandas as pd
import re
import string

csv_file = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Overdrive\\Beta\\all_3_lists2.csv"

df = pd.read_csv(csv_file)
#C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Overdrive
reg1 = r"/.*$"
#book list 1 = Philosophy
#book list 2 = Psychology
#book list 3 = Computer Technology

book1_titles = df.Classic_literature_title
book1_links = df.Classic_literature_link
book1_id_sorted = [[]]
book1_titles_sorted = [[]]
book2_titles = df.Psychology_title
book2_links = df.Psychology_link
book2_id_sorted = [[]]
book2_titles_sorted = [[]]

# print (book1_links[1])
# for i,x in enumerate(book1_links):
#     try:
#         x = x.replace("https://www.overdrive.com/media/","")
#         x = re.sub(reg1,"",x)
#         book1_links[i] = x
#     except AttributeError:
#         continue

for i,x in enumerate(book2_links):
    if book2_links[i].notnull():
        x = x.replace("https://www.overdrive.com/media/","")
        x = re.sub(reg1,"",x)
        book2_links[i] = x
        print (x)
    else:
        print ("Null"+x)
    # try:
    #     x = x.replace("https://www.overdrive.com/media/","")
    #     x = re.sub(reg1,"",x)
    #     book2_links[i] = x
    #     # print (x)
    # except AttributeError:
    #     print (x)

# for i,x in enumerate(book3_links):
#     try:
#         x = x.replace("https://www.overdrive.com/media/","")
#         x = re.sub(reg1,"",x)
#         book3_links[i] = x
#     except AttributeError:
#         continue

while len(book1_id_sorted) <= 9:
    book1_id_sorted.append([])
    book2_id_sorted.append([])
    # book1_titles_sorted.append([])

for i,x in enumerate(book1_links):
    if x[0].isdigit():
            book1_id_sorted[int(x[0])].append(x)
    # try:
    #     if x[0].isdigit():
    #         book1_id_sorted[int(x[0])].append(x)
            # book1_titles_sorted[int(x[0])].append(book1_titles[i])
    # except TypeError:
    #     continue

for x in book1_id_sorted:
    print (x)

for i,x in enumerate(book2_links):
    try:
        if x[0].isdigit():
            book2_id_sorted[int(x[0])].append(x)
            # book1_titles_sorted[int(x[0])].append(book1_titles[i])
    except TypeError:
        print (x)
#
#     # print (z)
#
# for i,x in enumerate(book2_links):
#     try:
#         if x in book1_id_sorted[int(x[0])]:
#             print (book2_titles[i]+"\t"+"https://www.overdrive.com/media/"+x)
#     except TypeError:
#         continue
