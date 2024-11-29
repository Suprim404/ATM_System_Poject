# ATM System
balance = 10000
pin = 2345

print("** Insert you card please**")
pin_num = int (input("Enter your pin please:\n"))
if pin_num == pin:
  while True:
    print('''
          1- Check Balance
          2- Deposite
          3- Withdraw
          4- Exit
          ''')
    option=int(input("Choose Your Option\n"))
    if option==1:
        print(f"Your current balance is {balance}")
    elif option ==2:
       deposit_amt=int(input("Enter your deposit amount\n"))
       balance= balance + deposit_amt
       print(f"Your updated balance is {balance}")
    elif option==3:
       withdraw_amt=int(input("Enter your withdrawl amount\n"))
       balance=balance-withdraw_amt
       print(f"Your Updated balance is {balance}")
    elif option==4:
       break
else:
  print("Pin Number is Wrong !!, Try Again")






  # print("** Insert you card please**")
# pin_num = int (input("Enter your pin please:\n"))
# if pin_num == pin:
#   print("Further processing....")
# else:
#   print("Pin Number is Wrong !!, Try Again")