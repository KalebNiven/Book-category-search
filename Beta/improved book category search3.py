
import re
import string

book1_title_input = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Overdrive\\Beta\\book1_title_output.txt"
book1_link_input = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Overdrive\\Beta\\book1_link_output.txt"

book2_title_input= "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Overdrive\\Beta\\book2_title_output.txt"
book2_link_input = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Overdrive\\Beta\\book2_link_output.txt"

reg1 = r"/.*$"
#book list 1 = Philosophy
#book list 2 = Psychology
#book list 3 = Computer Technology

book1_links = []
book2_links = []

book1_id_sorted = [[]]
book2_id_sorted = [[]]

book1_titles = []
book2_titles = []

with open (book1_link_input) as b1:
    content = b1.readlines()
    content = [x.strip() for x in content]
    for x in content:
        book1_links.append(x)
b1.close()

with open (book2_link_input) as b2:
    content = b2.readlines()
    content = [x.strip() for x in content]
    for x in content:
        book2_links.append(x)
b2.close()


with open (book1_title_input) as b1t:
    content = b1t.readlines()
    content = [x.strip() for x in content]
    for x in content:
        book1_titles.append(x)
b1t.close()

with open (book2_title_input) as b2t:
    content = b2t.readlines()
    content = [x.strip() for x in content]
    for x in content:
        book2_titles.append(x)
b2t.close()


for i,x in enumerate(book1_links):
        x = x.replace("https://www.overdrive.com/media/","")
        x = re.sub(reg1,"",x)
        book1_links[i] = x
        # print (x)

for i,x in enumerate(book2_links):
        x = x.replace("https://www.overdrive.com/media/","")
        x = re.sub(reg1,"",x)
        book2_links[i] = x
        # print (x)
#
# # for i,x in enumerate(book3_links):
# #     try:
# #         x = x.replace("https://www.overdrive.com/media/","")
# #         x = re.sub(reg1,"",x)
# #         book3_links[i] = x
# #     except AttributeError:
# #         continue
#
while len(book1_id_sorted) <= 9:
    book1_id_sorted.append([])
    book2_id_sorted.append([])
    # book1_titles_sorted.append([])
#
for i,x in enumerate(book1_links):
    if x[0].isdigit():
        book1_id_sorted[int(x[0])].append(x)
        # book1_titles_sorted[int(x[0])].append(book1_titles[i])
#
# for x in book1_id_sorted[x[0]]:
#     print (x)

# for i,x in enumerate(book2_links):
#     print (x)

# for i,x in enumerate(book2_links):
#     if x[0].isdigit():
#         book2_id_sorted[int(x[0])].append(x)
        # book1_titles_sorted[int(x[0])].append(book1_titles[i])

# #     # print (z)

for i,x in enumerate(book2_links):
    if x in book1_id_sorted[int(x[0])]:
        print (book2_titles[i]+"\t"+"https://www.overdrive.com/media/"+x)
