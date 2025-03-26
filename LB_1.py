import re

while True:
    author = input("author: ")
    if re.search(r'\d', author):
        print('ERROR WITH NAME')
    else:
        break

book = input("book: ")

Book_dict = {}

Book_dict = {
    "Author" : "Robert Shekli",
    "Name_book" : "Leech"
}

Book_dict[book] = author

for values in Book_dict.values():
    print(values)


