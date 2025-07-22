import csv
import pandas as pandasObj

# #read file operation
# # basic code 
# file=open("myFile.txt",'r')
# content = file.read()
# print(content)
# file.close() #close every file manually end of the file operation

# #read file operation
# #secure code use 
# #no need to close file manually 
# # with block automatically close the file
# #prevents memory leaks or file corruption
# with open("myFile.txt",'r') as file :
#     print(file.read())

# #readline is for work on first line until new line come \n
# with open("myFile.txt",'r') as file:
#     lines = file.readline()
#     print(lines)

# #readlines is return all text as a list every value is one line and end with \n if data have new line
# with open("myFile.txt",'r') as file:
#     lines = file.readlines()
#     print(lines)    

        
# # write operation
# # delete all content and add new content into file
# with open("myFile.txt",'w') as file:
#     file.write("new line add")

# # append operation
# # add new content into end of the file
# with open("myFile.txt",'a') as file:
#     file.write("append new line")

# write csv file
# newline='' use for remove extra new line gap after every row
with open("mycsvFile.csv",'w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name','marks'])
    writer.writerow(['mayuri',82])
    writer.writerow(['suyog',90])
    writer.writerow(['advik',81])

#read csv file using reader(reader is return each line data into seperated list(array) format)
with open("mycsvFile.csv",'r') as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)

#read csv file using reader(reader is return each line data into seperated dictonary(json) format)
with open("mycsvFile.csv",'r') as file:
    reader = csv.DictReader(file)
    for line in reader:
        print(line['name'])   

#read csv file using pandas and calculate avarage marks
file = pandasObj.read_csv("mycsvFile.csv")
print(file)
avarage = file['marks'].mean()
print(avarage)

