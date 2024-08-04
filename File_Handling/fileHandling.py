# rollno, name,age,  class , percentage

# 1. Writing into the file csv
# 2. Append more student into the file using the 'a'

import csv

f = open('C:\\Users\\anuj\\Desktop\\radhe.csv', 'a')

wo =  csv.writer(f, delimiter= ',')

n = int(input("Enter the no. of students: "))
lr = []

for i in range(n):
    rn = int(input("Enter RN? "))
    name = input("Enter name? ")
    age = int(input("Enter Age? "))
    clas = input("Enter class? ")
    percent = float(input("Enter percent? "))
    lr.append([rn, name, age, clas, percent])

wo.writerows(lr)

f.close()

