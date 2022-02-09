import io
from string import digits

f = io.open("full.txt", mode="r", encoding="utf-8")
file_string = f.read()

file_list = list(file_string.split("\n"))

#deleting nonalphabethical characters
def remove(list):
    list = [''.join(x for x in i if x.isalpha()) for i in list]
              
    return list

file_list = remove(file_list)

#filtering 5 character long words
result = [item for item in file_list if len(item)==5]

textfile = open("full_five_char.txt", mode="w+", encoding="utf-8")
for element in result:
    textfile.write(element + "\n")
textfile.close()
