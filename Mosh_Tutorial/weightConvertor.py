# weight = int(input("Weight? "))
# unit = input('(L)bs or (K)g:')

# if unit.upper() == 'L':
#     convert = weight * 0.45
#     print(f'Your weight is {convert} kilos')
# else:
#     convert = weight / 0.45
#     print(f'Your weight is {convert} pounds')


# ---------------------While loop-------------------------------#


# i = 1
# while i < 10:
#     print(i)
#     i = i+1
# print('Done')

#-------------------Car Game------------------------------------#

# command =""
# is_started = False
# print(""" 
#         Start --    to start the car
#         Stop --     to stop the car
#         quit --     to exit!
#     """)

# while command.lower() != "quit":
#     command = input("> ").lower()

#     if command == 'start':
#         if is_started:
#             print("Car is already Started....")
#         else:
#             is_started= True
#             print("Car Started.....")
#     elif command == 'stop':
#         if not is_started:
#             print("Car is already Stopped....")
#         else:
#             is_started = False
#             print("Car Stopped......")
#     elif command == 'quit':
#        break
#     else:
#         print("Sorry, I don't understand, enter right command.")



#-----------------------------For Loop---------------------------------------------#

# for item in range(0,10):
#     print(item)


# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')

