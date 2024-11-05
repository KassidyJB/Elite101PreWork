import random

name = input("What is your name? \n>")

print(f'\nWelcome to the Elitebot {name}!\n')

age = input(f'So {name}, how old are you?? \n>')

print(f'\nLord!! {age}!? That is so cool!!\n')


def display_menu():
  print(f' Anyways, it seems like you need help {name}.\n')
  print("1. Sign in") #Can use the sign in function to create saving and checking account 
  print("2. Log In") #Can use Log in to transfer, deposit, or withdraw money
  print("3. Learn More") #Gives user any additional details needed or anything they could learn
  print("4. Exit") #Exit the whole program (could be done with a while loop)

display_menu()
  
def selection():
  choice = int(input('''
  Enter your choice so I can properly assist. \n>'''))
  if choice == 1:
    print("Okay hold on,\n")
    choice_1()
  elif choice == 2:
    print("Let's get you started.\n")
    choice_2()
  elif choice == 3:
    print(f"Thank you for using JB BANK. See you next time, {name}!")
    choice_3()

selection()

def choice_1():
  user_name = input(f"{name}, Please enter a username for your new account below. \n")
  print(f"Hello {user_name}!
  
choice_1()

def choice_2():
  print("Why cant a statistic answer an algebraic question correct? Because it will PROBABLY get it wrong, hahahaha!!")
choice_2()

def choice_3():
  print(f"Thank you for using JB BANK. See you next time, {name}!")
choice_3()
  
selection()

#My Exit message works and still displays, yet it's an error
#I'll work on that as this course progresses.

