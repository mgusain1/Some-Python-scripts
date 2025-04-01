class Bank:
    def __init__(self,name,money):
        self.accountholder = name
        self.deposit = money
    
    def action(self,acc,money):
        if acc=="Deposit":
            self.deposit+=money
            print(f"Deposited ${money}, new account balance is ${self.deposit}")
        else:
            self.deposit-=money
            print(f"Withdrawn ${money}, new account balance is ${self.deposit}")
    def creditcheck(self):
        credit = int(input("Please give us our credit score"))
        if credit < 600:
            print("We cannot give you the loan")
        else:
            print("Yes we can give you the loan")
            
person = Bank("Maddy",650)
person.action("Withdraw",700)
person.creditcheck()


        
