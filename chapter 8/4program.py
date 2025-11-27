# Important

# Abstraction 
# hiding the implemantion details of class adn only showing the essential feature to the user.

# Encapsulation 
# wrapping data and function into a single unit(object).


# solving question 

class Account:
    def __init__ (self,bal,acc) :
        self.balance = bal
        self.account_no = acc

    def debit(self,amount):
        self.balance -= amount
        print("total balance " , self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("total balance " , self.get_balance())


    def get_balance(self) :
        return self.balance
    

acc1 = Account(10000, 12345)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(500)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)

