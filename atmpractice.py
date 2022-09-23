print("\t\t\t\t\t Welcome to HBL ATM DEPARTMENT")
atmpin=int(input("enter your pin"))
userdict={
     "useronepin":"1001",
     "useronename":"sehar"
}
print(userdict)
useronepin=1001
useronename="sehar"

#atmpin=int(input("enter your pin"))
if useronepin==atmpin:
    print("1.ADD MONEY")
    print("2.WithDraw")
    print("3.Change pin")
    print("4.Send MONEY")
else:
    print("you enter wrong pin")
my_choice=int(input("enter your choice"))
useronebalance=2000

def ADDMONEY():
     newbalance=int(input("enter your money you want to ADD:"))
     balance=useronebalance+newbalance
     print("your new balance is:",balance)
if my_choice==1:
   ADDMONEY()
def withdraw():
    newbalance = int(input("enter your money you want to withdraw:"))
    balance = useronebalance - newbalance
    print("your remaining balance is:", balance)
if my_choice==2:
    withdraw()
def changepin():
    newpin= int(input("enter your new pin:"))
    pin = useronepin + newpin
    print("your new pin is:", pin)
if my_choice == 3:
    changepin()

def sendmoney():
    newbalance = int(input("enter your money you want to send:"))
    balance = useronebalance - newbalance
    print("your remaining balance is:", balance)
    if newbalance<useronebalance:
        print("you can send money at any location")
    else:
      print(" you enter wrong choice")
if my_choice==4:
    sendmoney()





