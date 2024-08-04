class Atm:
    # constructor
    def __init__(self):
        self.pin = ""
        self.balance =0

        self.menu()

    def menu(self):
        user_input = input("""
            ********Choose Option*********
            1. Enter 1 to create pin
            2. Enter 2 to deposit
            3. Enter 3 to withdraw
            4. Enter 4 to chekc balance
            5. Enter 5 to Exit()
            
        """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            exit()
    
    def create_pin(self):
        self.pin = input("Enter your pin: ")
        print("Pin created successfully...")
    
    def deposit(self):
        tmp = input("Enter your pin: ")

        if tmp == self.pin:
            amount = int(input("Enter amount: "))
            self.balance = amount
            print("Deposit Successfully...")
        else:
            print("Invalid Pin...")
    
    def withdraw(self):
        tmp = input("Enter your pin: ")

        if tmp == self.pin:
            amount = int(input("Enter amount: "))

            if amount < self.balance:
                self.balance -= amount
                print("Withdraw Successfully...")
            else:
                print("Insufficient amount...")
        else:
            print("Invalid pin...")

    def check_balance(self):
        tmp = input("Enter your pin: ")
        if tmp == self.pin:
            print(self.balance)
        else:
            print("Invalid pin...")
    


a = Atm()