import random

print("--------------------------")
name = input("What is your name? \n>")

print(f'\nWelcome to JB Bank {name}!\n')

age = input(f'So {name}, how old are you?? \n>')

print(f'\nLord!! {age}!? That is so cool!!\n')

program_loop = True

def display_menu():
  print(f' Anyways, it seems like you need help {name}.\n')
  print("1. Sign in") #Can use the sign in function to create saving and checking account 
  print("2. Log In") #Can use Log in to transfer, deposit, or withdraw money
  print("3. Learn More") #Gives user any additional details needed or anything they could learn
  print("4. Exit") #Exit the whole program (could be done with a while loop)

display_menu()
  
def selection():
  in_use = True
  print("--------------------")
  choice = int(input('''
  Enter your choice so I can properly assist. \n>'''))
  if choice == 1:
    choice_1()
  elif choice == 2:
    choice_2()
  elif choice == 3:
    choice_3()
  elif choice == 4:
    print(f"Thank you for using JB BANK. See you next time, {name}!\n")
    print("------------------------")
    in_use = False

selection()

def choice_1():
  user_name = input(f"{name}, Please enter a username for your new account below. \n")
  print(f"Hello {user_name}!\n")
  cs_ask = input(f"{name}, would you like to create a savings or checking account?\n").capitalize()
  
  if cs_ask == "Savings":#So now, because I didn't have s or c capital, input HAS to be lowercase---->(fized using .capitalize())
    acc_select = input(f"Alright {user_name}, you selected Savings. Would you like to create a joint account or single account?\n").capitalize()
    
    if acc_select == "Single account":
    
    if acc_select == "Joint account":
  
  if cs_ask == "Checking account": 
    user_intel = []
    user_info = input(f"Enter your adress below, {user_name}\n").capitalize()
pass
#choice_1()

def choice_2():
  print("------------------------------------------------")
  log_name = input(f"Enter your username below, {name}")
  log_ask = input(f"{log_name}, would you like to transfer, deposit, or withdraw money?\n").capitalize()
  
  if log_ask == "Transfer":
    tran = float(input("How much money would you like to transfer?"))
  
  if log_ask == "Deposit":
    dep = float(input("How much money would you like to deposit?"))
  
  if log_ask == "Withdraw":
    wdraw = float(input("How much money would you like to withdraw?"))



pass

def choice_3():
  print("-------------------------------------")
  print(f"Here's a few things to know: \n")
  print('''Our ATM machines are located in each borough of NY, 7 in NJ, 
        4 in New Hampshire, and 3 in Pennsylvania''')
  print('''We at JB Bank prioritize your safety and will be the ones keeping your money in your pockets. 
        With that being said, you can earn up to $100 in your account by the end of each year you're with us. 
        Happy Banking!''')


pass

while program_loop:
  display_menu()
  program_loop = selection() 