try:
    num = int(input("Enter number? "))
    income = 30000
    percentage = int(input("Percentage? "))
    percent = income/percentage
    print(percent)
    print(num)
except ValueError:
    print("Invalid input....")
except ZeroDivisionError:
    print("Division error...")