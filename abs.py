from abc import ABC, abstractmethod

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
    
    @abstractmethod
    def withdraw(self,amtWithdraw):
        pass
        # if amtWithdraw >= self.__balance:
        #     print("No funds!")
        # else:
        #     self.__balance -= amtWithdraw


class SavingsAccount(BankAccount):

    def __init__(self, name, accno, balance, rate):
        super().__init__(name, accno, balance) # inherit from parent constructor
        self.__rate=rate


    def addInterest(self):
        interest = self.getBalance() * self.__rate/100
        self.deposit(interest)
        print("Saving interest added")

    def withdraw(self, amtWithdraw):
        if amtWithdraw > 50000:
            print("Saving account limit exceeded!")
        else:
            super().withdraw(self,amtWithdraw)



class CurrentAccount(BankAccount):
    def addInterest(self):
        interest = self.getBalance() * 0.01
        self.deposit(interest)
        print("Current interest added")

    def withdraw(self, amtWithdraw):
        print("Overdraft allowed in current account")
        super().withdraw(amtWithdraw)

class SalaryAccount(BankAccount):
    def addInterest(self):
        interest = self.getBalance() * 0.07
        self.deposit(interest)
        print("Salary interest added")

    def withdraw(self, amtWithdraw):
        if self.getBalance() - amtWithdraw < 1000:
            print("Minimum balance must remain 1000")
        else:
            super().withdraw(amtWithdraw)


gaurav_acc = SavingsAccount("Gaurav", 101, 5000000, 8)
ankur_acc = CurrentAccount("Ankur", 102, 50000)
sushant_acc = SalaryAccount("Sushant", 103, 50000)

acc = BankAccount("test", 100, 10000)


gaurav_acc.withdraw(100000)
gaurav_acc.show_details()
ankur_acc.withdraw(40000)
ankur_acc.show_details()
sushant_acc.withdraw(49500)
sushant_acc.show_details()
