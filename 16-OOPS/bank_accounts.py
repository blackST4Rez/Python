class BalancException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        
        print(f"\nAccount '{self.name} created.\nBalance = ${self.balance:.2f}'")
        
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        print("\nDesposit Complete.")
        self.getBalance()
        
    def viableTransaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalancException(
                f"\nSorry, account '{self.name}' only has balance of ${self.balance:.2f}"
            )
            
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw Complete.")
            self.getBalance()
        except BalancException as error:
            print(f'\nWithdraw Interrupted: {error}')
        
    def transfer(self, amount, account):
        try:
            print('\n**********\n\nBeginning Transfer..🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer Complete! ✅\n\n**********')
        except BalancException as error:
            print(f'\nTransfer interrupted. ❌ {error}')
            
class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit Complete.")
        self.getBalance()