password = '1234'
balance = 1000
count = 0
while True:
    ent_pass = input('enter your password: ')
    if ent_pass == password:
        print('account is logged in!')
        break
    elif count == 2:
        print('your account is frozen!!!')
        exit()
    else:
        print('wrong password')
        count += 1

while True:
    print('''======== ATM ========
    1. Check balance
    2. Deposit
    3. Withdraw
    4. Exit''')
    choice = input('enter your choice: ')
    if choice == '1':
        print("your balance is: " + str(balance))
    elif choice == '2':
        add = input("enter your amount of depositing: ")
        balance = balance + int(add)
    elif choice == '3':
        remove = input("enter your amount of withdrawing: ")
        if int(remove) > balance:
            print('not available!!')
        else:
            balance = balance - int(remove)
    elif choice == '4':
        print('Have an nice day!')
        break
    else:
        print('enter a valid choice: ')
