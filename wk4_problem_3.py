class BankAccount:
    def __init__(self, Account_number, Balance):
        self.Account_number = Account_number
        self.Balance = Balance
        def deposit(self, amount):
            if amount > 0:
                self.Balance += amount
            else:
                print ("Deposit amount must be positive.")
        def withdraw (self, amount):
            if amount > 0 and amount <= Balance:
                self.Balance -= amount
            elif amount >= Balance:
                print ("Error: insufficient funds")
            else:
                print ("Error: withdrawal amount must be positive")
        def get_Balance(self):
            return self.Balance
class SavingsAccount(BankAccount):
    def __init__(self, Account_number, Balance, interest_rate):
        super().__init__(Account_number, Balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        self.Balance += self.Balance * self.interest_rate
 
 bank_account_1 = BankAccount (1000, "1358")
 #same issue with the other code

print(bank_account_1.get amount())