
#TODO Creating a banking program that allows the user to check their balance, add money to their account, withdraw money from their account and will loop untit the option to quit is selected.

# TODO setting up the main menu of options 1.check balance 2. add money 3. withdraw money and 4. quit
# todo this function needs to loop



def main():
    name=input('\nEnter Name\n')
    password=input('\nEnter your pin number\n')
    password1=input('\nEnter your pin number again for validation\n')
    while password != password1:
        print("\npasswords do not match try again\n")
        password=input('\nEnter your pin number again\n')
        password1=input('\nEnter your pin number again for validation\n')
    else:
        print(f'\nHello {name} welcome to your account \n')



def pin():
    pin =input("\nplease re-enter your pin number to withdraw funds!\n")
    pin1=input('\nEnter your pin number again for validation\n')
    while pin != pin1:
        print('\nPIN NUMBERS DO NOT MATCH\n')
        print('\n NOT ABLE TO WITHDRAW FUNDS. THANK YOU COME AGAIN')






main()



user_selection = -2
current_balance = 750
# if anything but 4 is presses follow the option. If 4 is pressed quit.
while user_selection != 4:

    bal_greet = f'\nYour current balance is: ${current_balance}\n'
    user_selection = int(input('Hello, please choose one of following options:'
                               '\n 1) Check balance'
                               '\n 2) Add money to account'
                               '\n 3) Withdraw money from account'
                               '\n 4) Quit'
                               '\n What will you like to do?   '))
    if user_selection == 1:
        # show current balance
        print(bal_greet)
    # setting up option number 2 to add money to the account
    # add money to the current balance
    elif user_selection == 2:
        #Show the current balance before addition.
        print(bal_greet)
        # variable to ask how much to add to the accounty
        user_a = int(input('\nhow much money do you want to add to your account?  \n'))
        # add to the current balance in the account
        new_balance = (current_balance + user_a)
        # update the available balance to reflect the addition just made and keep that amount until the user leaves the app
        current_balance = new_balance
        # show what the current balance is after addition
        print(f'\nYour new balance is: ${new_balance}\n')

    elif user_selection == 3:
        #Show the current balance before withdrawl.
        print(bal_greet)
        #create variable that will hold the amount that is being withdrawn from the account.
        user_w = int(input('\nhow much money do you want to withdraw from your account?  \n'))
        # update the available balance to reflect the withdrawn funds just made and keep that amount until the user leaves the app
        pin()
        new_balance = (current_balance - user_w)
        # variable to hold the current account balance
        current_balance = new_balance
        #show the current account value
        print(f'\nYour new balance is: ${new_balance}\n')
        # if the account value is less than the amount that is trying to be withdrawn alert "insufficient funds"
        if user_w > current_balance:
            print('\nInsufficient Funds\n')
         # otherwhise show the current balance
        else:
            print(f'\nYour new balance is: ${new_balance}\n')
    # if a selection is made that is not 1-4 show an error message.
    else:
        print('\nMake a valid selection\n')
# test if 4 is selected, expecting print option below. Test of option 4 works.
print('Thank you for coming, see you later!')


### Challenge
# Before the program starts, ask the user for their account name and a pin number.
# - Instead of using "you", use the account user's name
# - Before allowing them to withdraw, check to see if they know the pin number. If they don't get the correct pin, ask them to try again.



