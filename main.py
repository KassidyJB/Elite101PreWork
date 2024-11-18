import random

name = input(f"What is your name? \n>")

print(f'\nWelcome to JB Bank {name}!\n')

age = input(f'So {name}, how old are you?? \n>')

print(f'\nLord!! {age}!? That is so cool!!\n')

def display_menu():
  print(f' \nNeed help? Choose an option below, {name}.\n')
  print("1. Sign in") #Can use the sign in function to create saving and checking account 
  print("2. Log In") #Can use Log in to transfer, deposit, or withdraw money
  print("3. Learn More") #Gives user any additional details needed or anything they could learn
  print("4. Exit") #Exit the whole program (could be done with a while loop)

program_loop = True
  
def selection():
  in_use = True
  print("________________________________________________")
  choice = int(input('Enter your choice so I can properly assist. \n>'))
  if choice == 1:
    choice_1()
  elif choice == 2:
    choice_2()
  elif choice == 3:
    choice_3()
  elif choice == 4:
    print(f"\nThank you for using JB BANK. See you next time, {name}!\n")
    print("______________________________________________")
    in_use = False
  else:
    print(f"\nInput may not be a number. Please try again!")
  return in_use
      

def choice_1():
  print("__________________________________________________________")
  user_name = input(f"\n{name}, Please enter a username for your new account below. \n>")
  print(f"\nHello {user_name}!\n")
  cs_ask = input(f"{user_name}, would you like to create a savings or checking account? \n>").capitalize()
  
  if cs_ask == "Savings":
    acc_select = input(f"\nAlright {user_name}, you selected Savings. Would you like to create a joint account or single account? \n>").capitalize()
    
    if acc_select == "Single account":
      print("_____________________________________________")

      user_intel_1 = []
      sav_add = str(input(f"\nEnter your address below, {user_name} \n>").capitalize())
      sav_social = str(input(f"Please enter your Social Security Number \n>"))
      sav_dob = str(input(f"\n What is your Date of Birth? \n>"))

      user_intel_1.append(sav_add)
      user_intel_1.append(sav_social)
      user_intel_1.append(sav_dob)
      print(user_intel_1)

      sav_ask = input(f"\nIs this info correct?\n>")

      if sav_ask == "No":
        print("Please restart this program.")
      elif sav_ask == "Yes":
        print("Great! You've created a Single Savings account. Thank you for using JB BANK Chatbot!")

    
    if acc_select == "Joint account":
      print("___________________________________________")
      user_info = []

      address = str(input(f"\nEnter your address below, {user_name}\n>").capitalize())
      user_info.append(address)

      social = str(float(input(f"\nPlease enter your Social Security Number\n>")))
      user_info.append(social)

      DOB = str(input(f"\nWhat is your Date Of Birth?\n>"))
      user_info.append(DOB)
      print(user_info)
      joint_ask = input(f"\nIs this info correct?\n>")

      if joint_ask == "No":
        print(f"\nPlease restart this program\n")
      elif joint_ask == "Yes":
        print(f"\nAlright.\n")
        clarify = input(f"\nJust to be sure, you're creating a joint account with a partner or guardian?\n>").capitalize()
        if clarify == "No":
          print(f"\nPlease restart this program, you've entered the wrong section.\n")
        elif clarify == "Yes":
          print(f"\nGreat! You've created a Joint Savings account. Thank you for using JB BANK Chatbot!\n")
      
  
  elif cs_ask == "Checking": 
    print("______________________________________________________")
    checking = []
    c_add = str(input(f"\nEnter your adress below, {user_name} \n>").capitalize())
    checking.append(c_add)

    c_social = str(input(f"\nPlease enter your Social Security Number \n>"))
    checking.append(c_social)

    c_dob = str(input(f"\nWhat is your DOB?\n>"))
    checking.append(c_dob)

    print(checking)
    check_ask = input(f"\nIs this information correct? \n>")
    



def choice_2():
  print("______________________________________________________________")
  log_name = input(f"\nEnter your username below, {name} \n>")
  log_ask = input(f"\n{log_name}, would you like to transfer, deposit, or withdraw money? \n>").capitalize()
  actions = []
  if log_ask == "Transfer":

    tran = (str(float(input(f"\nHow much money would you like to transfer? \n>"))))
    actions.append(tran)
    print(f"{tran} dollars transferred.")
  
  if log_ask == "Deposit":
    dep = (str(float(input(f"\nHow much money would you like to deposit? \n>"))))
    actions.append(dep)
    print(f"{dep} dollars added to your account.")

  if log_ask == "Withdraw":
    wdraw = (str(float(input(f"\nHow much money would you like to withdraw? \n>"))))
    actions.append(wdraw)
    print(f"{wdraw} dollars withdrawed.")





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
