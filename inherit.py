class BankAccount:
    bankName = "HDFC Bank"

    def __init__(self, name, accno, balance):
        self.name = name
        self.accno = accno
        self.__balance = balance

    def show_details(self):
        print("Name: ", self.name)
        print("Account No.: ", self.accno)
        print("Balance: ", self.__balance)

    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount} deposited successfully.")

    def getBalance(self):
        return self.__balance
    
    def withdraw(self,amtWithdraw):
        if amtWithdraw >= self.__balance:
            print("No funds!")
        else:
            self.__balance -= amtWithdraw


class SavingsAccount(BankAccount):

    def __init__(self, name, accno, balance, rate):
        super().__init__(name, accno, balance) # inherit from parent constructor
        self.rate=rate

    def addInterest(self):
        interest = self.getBalance() * self.rate/100
        self.deposit(interest)
        print("Saving interest added")

class CurrentAccount(BankAccount):
    def addInterest(self):
        interest = self.getBalance() * 0.01
        self.deposit(interest)
        print("Current interest added")

class SalaryAccount(BankAccount):
    def addInterest(self):
        interest = self.getBalance() * 0.07
        self.deposit(interest)
        print("Salary interest added")


gaurav_acc = SavingsAccount("Gaurav", 101, 5000000, 8)
ankur_acc = CurrentAccount("Ankur", 102, 50000)
sushant_acc = SalaryAccount("Sushant", 103, 50000)


gaurav_acc.addInterest()
ankur_acc.addInterest()
sushant_acc.addInterest()


gaurav_acc.show_details()
ankur_acc.show_details()
sushant_acc.show_details()
