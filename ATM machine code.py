#ATM
name="umadevi"
password="123"
user_name = input("Enter the user Name:")
password = input("Enter the password:")
s='''
 1.credit
 2.debit
 3.mini statement
 4.Exit
'''

Amount= 1000
if name ==user_name and password==password:
    while True:
        print(s)
        option=int(input("Enter the option:"))
        if option==1:
             credit_amount=float(input("Enter the Amount:"))
             print("Amount after credit:")
        if option==2:
             debit_amount=float(input("Enter the Amount:"))
             print("Amount after debit:",Amount-debit_amount)
        elif option==3:
             print("Amount:",Amount)
        elif option==4:
              break
else:
    print("incorrect")