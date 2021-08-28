class User:
    def __init__(self, username, email_address):
        self.name = username			
        self.email = email_address		
        self.account_balance = 0		

    def make_withdrawal(self, amount):
        self.account_balance -= amount	

    def display_user_balance(self):
        self.account_balance
    
    def make_deposit(self, amount):	
        self.account_balance += amount

guido = User("Guido van Rossum", "guido@python.com")
Catalan = User("Forca Barca", "FCB@python.com")
BucksFan = User("Deer District", "BUCKS@python.com")

guido.make_withdrawal(100)
guido.make_deposit(100)
guido.make_deposit(100)
guido.make_deposit(100)
Catalan.make_deposit(100)
Catalan.make_deposit(100)
Catalan.make_withdrawal(50)
Catalan.make_withdrawal(50)
BucksFan.make_deposit(100)
BucksFan.make_withdrawal(25)
BucksFan.make_withdrawal(25)
BucksFan.make_withdrawal(25)
print(guido.account_balance)
print(Catalan.account_balance)
print(BucksFan.account_balance)	
# class User:
    # pass    # we'll fill this in shortly
# michael = User()
# anna = User()

# class User:		# declare a class and give it name User
#     def __init__(self):
#         self.name = "Michael"
#         self.email = "michael@codingdojo.com"
#         self.account_balance = 0

# guido = User()
# monty = User()

# print(guido.name)	# output: Michael
# print(monty.name)	# output: Michael

# class User:
#     def __init__(self, username, email_address):# now our method has 2 parameters!
#         self.name = username			# and we use the values passed in to set the name attribute
#         self.email = email_address		# and the email attribute
#         self.account_balance = 0		# the account balance is set to $0, so no need for a third parameter
#         # adding the deposit method
#     def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
#         self.account_balance += amount	# the specific user's account increases by the amount of the value received

# guido = User("Guido van Rossum", "guido@python.com")
# monty = User("Monty Python", "monty@python.com")

# guido.make_deposit(100)
# guido.make_deposit(200)
# monty.make_deposit(50)
# print(guido.account_balance)	# output: 300
# print(monty.account_balance)	# output: 50




# print(guido.name)	# output: Guido van Rossum
# print(monty.name)	# output: Monty Python

    
    

# python user.py



