file = open("student.txt",'r')

# for line in file:
    
#     print(line.strip())

content = file.read()
print(content)

file.close()