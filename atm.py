
class ATM:
    def __init__(self,atmNumber,pinNumber):
        self.atmNumber = atmNumber
        self.pinNumber = pinNumber

        def check_balance(self):
            print("your balance is 10000 Rupees")

        def withdrawl(self,amount):
            new_amount = 10000 - amount
            print(amount+"has been withdrawn")   
    def main():
        cardNumber = input("insert your card number")
        pin = input("enter your pin number")

        holder = ATM(cardNumber,pin) 

        print("choose activity")
        print("1. Balance Check  2.Withdraw")
        activity = int(input("enter activity number."))

        if(activity == 1):
            holder.check_balance()
        elif(activity == 2 ):
            amount = int(input("enter amount"))
            holder.withdrawl(amount)
        else:
            print("enter a valid number")

    