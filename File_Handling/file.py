# age = input("enter your age? ")

# file = open("data.txt", 'w')

# file.write(age)
# file.close()

# f = open('data.txt', 'r')
# print(f.read())

# f.close()

# file = open('example.txt', 'w')

# # Writing to the file
# file.write("Hello, World!\n")
# file.write("This is a file handling example in Python.")

# # Closing the file
# file.close()

file = open("student.txt", 'aS')

#writing to file
name = input("Enter name: ")
age = input("Age: ")
course = input("Course: ")
rollno = input("RollNo: ")

# data = """ Your name is {name}
# Age: {age}
# Course: {course}
# Roll No: {rollno}
# """
file.write(f'Name: {name}\n Age: {age}\n Course: {course} \n Roll-No: {rollno}\n')

file.close()