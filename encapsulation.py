class BankAccount :
    def __init__(self, name, balance) :
        self.name = name #public
        self._balance = balance #protected

    def get_balance(self) : #getter
        return self._balance
    
    def set_balance(self, newBalance) : #setter
        self._balance = newBalance

acc1 = BankAccount("Hemant", 20_0000)

acc1.set_balance(50_0000)
print(f"{acc1.name} your acccount balance is Rs.{acc1.get_balance()} ")
