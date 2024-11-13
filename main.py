import random

program_loop = True

name = input(f"What is your name? \n>")

print(f'\nWelcome to JB Bank {name}!\n')

age = input(f'So {name}, how old are you?? \n>')

print(f'\nLord!! {age}!? That is so cool!!\n')

def display_menu():
  print(f' \nAnyways, it seems like you need help {name}.\n')
  print("1. Sign in") #Can use the sign in function to create saving and checking account 
  print("2. Log In") #Can use Log in to transfer, deposit, or withdraw money
  print("3. Learn More") #Gives user any additional details needed or anything they could learn
  print("4. Exit") #Exit the whole program (could be done with a while loop)

display_menu()
  
def selection():
  in_use = True
  print("------------------------------------------")
  choice = int(input('Enter your choice so I can properly assist. \n>'))
  if choice == 1:
    choice_1()
  elif choice == 2:
    choice_2()
  elif choice == 3:
    choice_3()
  elif choice == 4:
    print(f"\nThank you for using JB BANK. See you next time, {name}!\n")
    print("---------------------------------------")
    in_use = False

def choice_1():
  print("------------------------------------------------")
  user_name = input(f"\n{name}, Please enter a username for your new account below. \n>")
  print(f"\nHello {user_name}!\n")
  cs_ask = input(f"\n{name}, would you like to create a savings or checking account? \n>").capitalize()
  
  if cs_ask == "Savings":
    acc_select = input(f"\nAlright {user_name}, you selected Savings. Would you like to create a joint account or single account? \n>").capitalize()
    
    if acc_select == "Single account":
        user_intel_1 = []
        user_info_1 = input(f"\nEnter your address below, {user_name} \n>").capitalize()
    
    if acc_select == "Joint account":
      user_intel_2 = []
      user_info_2 = input(f"\nEnter you address below, {user_name} \n>").capitalize()
      user_intel_2.append(user_info_2)
  
  if acc_select == "Checking account": 
    user_intel_3 = []
    user_info = input(f"\nEnter your adress below, {user_name} \n>").capitalize()
    user_intel_3.append(user_info)




def choice_2():
  print("------------------------------------------------")
  log_name = input(f"\nEnter your username below, {name} \n>")
  log_ask = input(f"\n{log_name}, would you like to transfer, deposit, or withdraw money? \n>").capitalize()
  
  if log_ask == "Transfer":
    tran = float(input(f"\nHow much money would you like to transfer? \n>"))
  
  if log_ask == "Deposit":
    dep = float(input(f"\nHow much money would you like to deposit? \n>"))
  
  if log_ask == "Withdraw":
    wdraw = float(input(f"\nHow much money would you like to withdraw? \n>"))



def choice_3():
  print("--------------------------------------------------------------")
  print(f"\nHere's a few things to know: \n")
  print(f'''\nOur ATM machines are located in each borough of NY, 7 in NJ, 
  4 in New Hampshire, and 3 in Pennsylvania \n''')
  print(f'''\nWe at JB Bank prioritize your safety and will be the ones keeping your money in your pockets. 
  With that being said, you can earn up to $100 in your account by the end of each year you're with us. 
  Happy Banking!''')


while program_loop:
  display_menu()
  program_loop = selection() 