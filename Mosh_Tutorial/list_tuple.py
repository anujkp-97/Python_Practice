# names = ['anuj', 'keshav', 'shiv', 'krishna', 'arjun']


# for name in names:
#     count = len(name)
#     c =0
#     while c <= count:
#         print('*' * c)
#         c = c+1

# print(names[-1])

# numbers = [3,6,1,4,8,10, 11, 7, 3]
# max = numbers[0]

# for num in numbers:
#     if max < num:
#         max = num

# print(max)


#---------------------------------------2D List----------------------------------#


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


print(matrix)

print(matrix[0])
print(matrix[0][1])

print("Remove Duplicates from the list")

numbers =[2,3,4,2,5,6,4,]
unique =[]

for number in numbers:
    if number not in unique:
        unique.append(number)

print(unique)
