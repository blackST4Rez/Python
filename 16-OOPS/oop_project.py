from bank_accounts import *

Raka = BankAccount(1000, "Raka")
Hari = BankAccount(2000, "Hari")

Raka.getBalance()
Hari.getBalance()

Raka.deposit(800)
Hari.deposit(250)

Raka.withdraw(5)

Raka.transfer(2.8, Hari)

Jim = InterestRewardsAcct(1000, "Jim")
Jim.getBalance()
Jim.deposit(100)

Jim.transfer(100, Raka)

