class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def withdraw(self, amount):
        self.balance = self.balance - amount

alice_account = BankAccount("Alice", 1000)
bob_account = BankAccount("Bob", 500)

print(alice_account.balance)    
print(bob_account.balance)      

alice_account.deposit(200)
print(alice_account.balance)    

bob_account.withdraw(100)
print(bob_account.balance)      