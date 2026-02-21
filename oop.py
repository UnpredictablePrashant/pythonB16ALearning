class BankAccount:

    def __init__(self, name, accno, balance):
        self.name = name
        self.accno = accno
        self.balance = balance

    def __del__(self):
        print("Account closed")

    def show_details(self):
        print("Name: ", self.name)
        print("Account No.: ", self.accno)
        print("Balance: ", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully.")

    def getBalance(self):
        return self.balance


abash_acc = BankAccount("Abhash", 123412415324, 20000)
sharath_acc = BankAccount("Sharath", 4121313123, 50000)

# print(abash_acc.name, abash_acc.accno)
abash_acc.show_details()
abash_acc.deposit(6000)
# abash_acc.show_details()
print("Current Balance: ", abash_acc.getBalance())

# del abash_acc
