print("|=============================================================================|")  
while True:
    try:
        name_1 = input("|* Please enter your name: |")
        if name_1.isalpha():
          break
        else:
          print("|---------------------------------------------------------------------|")
          print("|         Please enter a name with letters only, and dont leave empty |")
          print("|---------------------------------------------------------------------|")
          
      
    except ValueError:
        print("|        Please Enter a name with letters only, and dont leave empty            |")

print("|=============================================================================|") 
def welcome_MCQ_quiz():
  print("|=============================================================================|") 
    
  print("|*****************************************************************************|")


  print("|*                                                                           *|")
  print("|                   Hello {}, Welcome to My Math Quiz 2022.                    |\n|            Please enter in your answer if the AI prompts you to do so,      |\n|         and please read the rules. Please note that this quiz is designed   |\n|       specifically for year 11 students, so if you are in year 10 or below  |\n|          and/or above, you will either find it tough or simple.             |\n|                       \033[4mNote\033[0m -'^' = to the power of                           |\n|                          Good Luck have fun!!                               |" .format(name_1))
  
  
  print("|*****************************************************************************|")
  print("|=============================================================================|") 
  input("press Enter to continue to start questions ...")
  play_MCQ_quiz()
  print("|=============================================================================|") 

#i could   

import random


questions = {'|*               Solve Following Equation   \n|         2x(3x+4) \n|    a: 6x^2+8x \n|    b: 5x^2+8x\n|    c: 5x+8x\n' : 'a' ,
'|*               Question 2                              \n|     9x(12x+18) \n|    a: 21x^2+27x  \n|    b: 108x^2+162x\n|    c: 9x+30x \n' :  'b' , 
'|*               Question 3 \n|    a: answer a\n|    b: answer b\n|    c: answer c \n' : 'c' }


def play_MCQ_quiz():
 score = 0
 
 k = list(questions)
 random.shuffle(k)
 for key in k:
  print("|*****************************************************************************|")
  print("|                                                                             |")
  print(key)
  print("|                                                                             |")
  print("|*****************************************************************************|")
  print("|=============================================================================|")
  user_answer = input("|*     Enter A, B or C: |").lower().strip()
  print("|=============================================================================|")
  if questions.get(key) == user_answer:
          print("                                          |-------------------------------|     ")
          print("                                          |         Correct!              |     ")  
          print("                                          |-------------------------------|     ")
          score =  score + 1
  else:
          print("                                          |-------------------------------|     ")
          print("                                          |        Incorrect :(           |     ")
          print("                                          |-------------------------------|     ")
 print("| Your Final Score is:  " + str(score))



def main_menu():
  print("|*****************************************************************************|")
  print("|                                                                             |")
  print("|                     WELCOME TO THE MATH QUIZ 2022                           |")
  print("|                                                                             |")
  print("|*****************************************************************************|")
  print("|                       Please select an option:                              |")
  print("|*                                                                           *|")
  print("|                       1. Play Math quiz                                     |")
  print("|                       2. Know the rules                                     |")
  print("|                       3. Quit                                               |")
  
  print("|*                                                                           *|")
  print("|*****************************************************************************|")
  print("|=============================================================================|")
  while True:
    try:
       choice = input("|*      Enter 1,2 or 3: |")
       if choice == 1 or 2 or 3: 
            break
       else:
         print("|----------------------------------------------------------------------|")
         print("|                     Not a Valid Integer! Please Only Enter 1, 2 or 3 |" )
         
         print("|----------------------------------------------------------------------|")
    except ValueError:
        print("Not a valid integer! Please try again ...")



 




  
  if choice == "1":
    welcome_MCQ_quiz()
  elif choice == "3":
    print("Thanks for Playing :) !")
    quit()
  elif choice == "2":
    print("|=============================================================================|")
    print("|*****************************************************************************|")
    print("|                     Here are 3 simple rules :                               |")
    print("|*                                                                           *|")
    print("|                     1. No cheating                                          |")
    print("|                     2. Only calculators are  allowed if necessary           |")
    
    print("|                     3. Have Fun!!                                           |")
    print("|*                                                                           *|")
    print("|*****************************************************************************|")
    print("|=============================================================================|") 
    input("|*     Press Enter To Continue...")
    print("|=============================================================================|") 
    welcome_MCQ_quiz()
  


main_menu()


