class BankAccount:
    def __init__(self):
        self.balance=0
        self.accountOpen=0

    def get_balance(self):
        if self.accountOpen==1:
            return self.balance
        else:
            raise ValueError("account not open")

    def open(self):
        if self.accountOpen!=1:
            self.accountOpen=1
        else:
            raise ValueError("account already open")           
    

    def deposit(self, amount):
        if self.accountOpen==1:
            if amount>=0:
                self.balance+=amount
            else:
                raise ValueError("amount must be greater than 0")    
        else:
            raise ValueError("account not open")    

    def withdraw(self, amount):
         if self.accountOpen==1:
            if amount>=0:
                if amount <=self.balance:
                    self.balance-=amount
                else:
                    raise ValueError("amount must be less than balance")
            else:
                raise ValueError("amount must be greater than 0") 
         else:
           raise ValueError("account not open")

    def close(self):
        if self.accountOpen==1:
            self.accountOpen=0
            self.balance=0
        else:
           raise ValueError("account not open")

    
