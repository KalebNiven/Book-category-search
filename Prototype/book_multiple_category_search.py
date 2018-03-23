import string
import csv
import pandas as pd


book_list_file_1 = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Overdrive\\Psychology_books.txt"
book_list_file_2 = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Overdrive\\Computer_Technology_books.txt"
book_list_file_3 = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Overdrive\\Philosophy_books.txt"

csv_file = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Overdrive\\all_3_lists.csv"
df = pd.read_csv(csv_file)



#C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Overdrive
book1_titles = []
book1_links = []
book2_title = []
book2_links = []
book3_links = []




# a = [["1.2",'abc',"3"],["1.2",'werew',"4"]]   #testing writing to csv

book_list_1 = []    #the first book list

book_list_1_alphabetical = [[]]  #the first book sorted into separate lists by first letter of book

book_list_2 = []


with open(book_list_file_1) as r:
    content = r.readlines()
    for x in content:
        x =x.strip()
        book_list_1.append(x)
r.close()

with open(book_list_file_2) as f:
    content = f.readlines()
    for x in content:
        x =x.strip()
        book_list_2.append(x)
f.close()

book_list_1 = sorted(book_list_1)
# print(string.ascii_lowercase[4])
for x in book_list_1:
    for i,z in enumerate(string.ascii_lowercase):
        if x.startswith(z.upper() or x.startswith(z)):
            book_list_1_alphabetical[i].append(x)
            break
        if len(book_list_1_alphabetical) <= 52:
            book_list_1_alphabetical.append([])

# for x in book_list_1_alphabetical:
#     print (x)

def book_starts_with(book):
    begins_with = 27
    for i,z in enumerate(string.ascii_lowercase):
        if book.startswith(z.upper() or book.startswith(z)):
            begins_with = i
    return begins_with

# for x in book_list_1_alphabetical:
#     print (x)

# final = []
# print (book_list_2)
# print("-----------")
# for x in book_l/ist_1_alphabetical[book_starts_with(x)])

# search by what book starts with in other list
for i,x in enumerate(book_list_2):
    if x in book_list_1_alphabetical[book_starts_with(x)]:
        # print ("j: "+str(j)+"  "+"z: "+z+"\t:\t"+"i: "+str(i)+ " "+"x: "+x)
        # print("i: "+str(i)+ " "+"x: "+x)
        print(x)


# resultFile = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Overdrive\\alphabetical_test2.csv"
# with open(resultFile, "wb") as f:
#     writer = csv.writer(f)
#     writer.writerows(a)
# f.close()

# my_df = pd.DataFrame(book_list_1_alphabetical)
# my_df.to_csv('alphabetical_test2.csv', index=False, header=False)
