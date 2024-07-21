# Dictionay is use with data having key-value pair, 
# Duplicate is not allowed in the dictionary



# customers = {
#         'name': 'Anuj Kumar',
#         'age' : 24,
#         'email' : 'anujpal78@gmail.com',
#         'address' : 'India',
#         'is_verified' : True
# }

# print(customers['name'])
# print(customers.get('birth'))

# for info in customers:
#     print(info.upper())

numbers = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine"
}

phone = input("Phone? ")
output = ""

for ch in phone:
    output += numbers.get(ch, " !  " + "  ")


print(output)



