import random#this is so that all the questions if the user would like to retake the quiz in the future they do not come in the same order
#The user's name is requested in the section below. I've used the while true function to ensure that it runs quickly (loops) if the user types in an invalid name, such as a number.
def start():
  while True:
        global name_1 
        name_1 = input("| Please enter your name: |")
        if name_1.isalpha():#If the user hasn't written their name in alphabetical order, this method breaks it and displays the error message below. Following the error statement, the code uses the while loop to print out the name statement once more.
          break
        else:
          # start for asking the users name
          print("|---------------------------------------------------------------------|")
          print('')
          print("|         Please enter a name with letters only, and dont leave empty |")
          print('')
          print("|---------------------------------------------------------------------|")



def main_menu():
  print("|-----------------------------------------------------------------------------|")
  print("|                                                                             |")
  print("|                     WELCOME {} TO MY MATHS QUIZ MADE IN 2022                 |".format(name_1))
  print("|                                                                             |")
  print("|-----------------------------------------------------------------------------|")
  input("|                     |Please Click Enter To Continue| ")
  print("|This quiz was made and devolped by Kavish Prakash   |")
  input("|                     |Please Click Enter To Continue| ")
  print("|-----------------------------------------------------------------------------|")
  print("|                       Please select an option:                              |")
  print("|                                                                             |")
  print("|                       1. Play Math quiz                                     |")
  print("|                       2. Know the rules                                     |")
  print("|                       3. Quit                                               |")
  print("|-----------------------------------------------------------------------------|")
  print("|-----------------------------------------------------------------------------|")
  #this is to select the options in the menu 1= PLay quiz 2= know the rules 3= Quit  quiz
  while True: 
    try:
       choice = input("|       Enter 1,2 or 3: |")
       if choice == 1 or 2 or 3:
            break
       else:
         print("|----------------------------------------------------------------------|")
         print("|                     Not a Valid Integer! Please Only Enter 1, 2 or 3 |" )
         
         print("|----------------------------------------------------------------------|")
    except ValueError:
        print("Not a valid integer! Please try again ...")
#This section below contains codes that I want quiz to run  if they type in 1,2, or 3. For example, if they write 1, the quiz will lead them to the welcome statement , which is part of the welcome MCQ quiz function (). If 3 , it prints "thank you" and then exits. If the answer is 2, it will publish everything that is related to the that option.
  
  if choice == "1":
    welcome_MCQ_quiz()
  elif choice == "3":
    print("Thanks for Playing :) !")
    quit()
    # this is to run thanks for playing right at the end of the quiz to thank the player
  elif choice == "2":
    print("|-----------------------------------------------------------------------------|")
    print("|-----------------------------------------------------------------------------|")
    print("|                     Here are 3 simple rules :                               |")
    print("|                     1. No cheating                                          |")
    print("|                     2. Only calculators are allowed                         |")
    
    print("|                     3. No raging                                            |")
    print("|-----------------------------------------------------------------------------|")
    print("|-----------------------------------------------------------------------------|")
    input("|                     |Please Click Enter To Continue| ")
    print("|-----------------------------------------------------------------------------|") 
  # that is the rules menu

  
#starting of running program






def welcome_MCQ_quiz(): #<This function not only defines the welcome statement, but it also saves whatever I want within it. This simplifies things since all I have to do now is call welcome MCQ quiz(), and it will perform all of the tasks in this function.
  print("|-----------------------------------------------------------------------------|") 
    
  print("|-----------------------------------------------------------------------------|")


  print("|                                                                             |")
  print("|                   Hello {}, Welcome to My Math Quiz 2022.                    |\n|           Please note that this quiz is designed                            |\n|     specifically for year 11 students, so don't be disheartened             |\n|           if the results  arent up to your standards                        |\n|                       \033[4mNote\033[0m -'^' = to the power of                           |\n|                          Good Luck have fun!!                               |" .format(name_1)) #This.format function takes the place of #variable. It will place their name after the "hello" in this example since it has this ""which implements that specific variable answer in that specific section (name 1 is where the code asks for the user name).
  
  
  print("|-----------------------------------------------------------------------------|")
  print("|-----------------------------------------------------------------------------|") 
  input("|       Press Enter To Continue To Start Questions")
  play_MCQ_quiz() # The play MCQ quiz function starts with questions and records any essential information, such as value errors, before asking the user to input their response and double-checking their answer against my dictionary values. This simplifies things since all I have to do now is add a define statement, and when I call it, it will complete all of the chores that the define function contains.
  print("|=============================================================================|") 



#starting  of the quiz
 


#This variable below holds all of my math questions, which I found using a dictionary. My keys and values are kept in a dictionary; in this case, the keys are the math questions that are contained in the variable questions, and the value is the answers to those arithmetic questions.
#Not only does this function create the welcome statement, but it also saves any data I want to include in it. This simplifies things because now all I have to do is call welcome MCQ quiz(), and it will take care of the rest.
  print("|-----------------------------------------------------------------------------|") 
    
  print("|-----------------------------------------------------------------------------|")


  print("|                                                                             |")
  print("|                   Hello {}, Welcome to My Math Quiz 2022.                    |\n|                  Please note that this quiz is designed                     |\n|   specifically for year 11 students, don't be dishearten if the results     |\n|               aren't up to your standards                                   |\n|                       \033[4mNote\033[0m -'^' = to the power of                           |\n|                          Good Luck have fun!!                               |" .format(name_1))
  
#variable has been replaced with #this.format. Because it has this ""which implements that specific variable answer in that specific area, it will insert their name after the "hello" in this case (name 1 is where the code asks for the user name).

 
 

questions = {'|*               Solve Following Equation   \n|         2x^2 – 3xy when x = –3 and y = 4 \n|    a: 54 \n|    b: 69 \n|    c: 52' : 'a' ,
'|*              Solve Following Equation                            \n|     w^4 – 18w^2 + 81 = 0 \n|    a: -9, 9  \n|    b: -3. 3\n|    c: -6x 6 \n' :  'b' , 
'|*               Solve the inequality \n|         (3x + 2)(2x – 1) ≤ (6x + 1)(x – 3)\n     a: x < -1/8\n|    b: 18x < -1 \n|    c: x < -1/18 \n' : 'c' , '|*               Solve the equation \n|         x+2/3 - 2x-1/5 = 1\n    a: x = -1 \n|    b: x = 2 \n|    c: x = -2 \n' : 'c' ,'|*         Solve the equation \n|     2/x-3 - 2/x-1 = 3/x+5 \n|    a: x = 7 \n| b: x = 6\n|    c: x=8 \n' : 'a' ,'|*               Calculate the Probability   \n|         Levi’s father says that, when he was the same age, his chance of    |\n|scoring was 60% If Levi’s father had taken 200 shots when he was the same age|\n| how many shots would he have scored on? \n|    a: around 120 \n|    b: around 140 \n|    c: around 100' : 'a' ,'|*               Calculate the Probability   \n|         75% of homes on the national power supply in New Zealand are in the |\n|North Island. The rest are in the South Island.70% of homes in the North     |\n|Island and 80% of homes in the South Island use electricity for their heating|\n|Calculate the probability that a home selected randomly across New Zealand is|\n|on the national power supply in the North Island AND uses electricity for    |\n| heating. \n|    a: 21/40 \n|    b: 25/40 \n|    c: 36/40' : 'a' ,'|*               Solve following problem  \n|Leo is laying square concrete tiles for his deck. He starts with laying them |\n|down to form a square pattern, but his friend thinks it would be better if   |\n|they were laid out to form a rectangle. He changes his layout to make the    |\n|length of the deck 6 tiles longer, and the width of the deck 4 tiles shorter.|\n|He finds he needs 2 extra tiles to complete the rectangular pattern.How many |\n| tiles did he have to start with? \n|    a: 13 \n|    b: 169 \n|    c: 48' : 'b' ,'|*               Solve following problem   \n|         Tane and Pete are raising funds for their sports trip. Between them |\n|they need to raise $1000.There are only 5 weeks until they need the money.   |\n|Tane gets paid $15 an hour, and Pete gets paid $16 an hour as he has more    |\n|experience. Between them they work for a total of 13 hours each week.What is |\n|the average number of hours that each of them work per week if they are to   |\n|have exactly the amount of money they need? \n|    a: Pete = 5h & Tane = 10h \n|    b: Pete = 4h & Tane = 7h \n|    c: Pete = 5h & Tane = 8h' : 'c' ,'|*               Solve following problem    \n|         Mere gives some clues so that her secret number can be calculated.  |\n|She says, “When 20 is divided by my secret number and then 7 is added to this|\n|answer, this gives a solution of 2.” What is Mere’s secret number?           | \n|    a: -8 \n|    b: -4 \n|    c: 8' : 'b' ,}


def play_MCQ_quiz(): #This function checks for problems, prints keys from the dictionary, and asks for a response from the user. I've put everything in a define statement so that all I have to do now is call play MCQ quiz() and it will run everything. This function prints out arithmetic questions, then prompts the user for an answer, which is then verified as correct or incorrect.
 score = 0 #Algebra, Chance n Data, Teg
  
 k = list(questions)
 random.shuffle(k)# this shuffles the variable "k", throughout the question
 for key in k:  #This function calls the keys (math questions) in my variable "questions" through the variable "k," which is the variable that randomises the order of my questions. 
  print("|*****************************************************************************|")
  print("|                                                                             |")
  print(key)
  print("|                                                                             |")
  print("|*****************************************************************************|")
  print("|=============================================================================|")
 

   
 
  while True: 
    try:
       user_answer = input("|*     Enter A, B or C: |").lower().strip()   #The responses are saved in the variable user answer. Lower and strip ensure that the code receives the correct response since lower changes the user's response to lower case, which matches my dictionary entry and ensures accuracy, and strip avoids additional spaces if the user has accidentally included one.
       if user_answer == 'a': 
           break
       elif user_answer == 'b':
           break
       elif user_answer == 'c':
           break
        
       else: 
         print("|---------------------------------------------------------------------|")
         print("|        Please only Enter A, B or C and dont leave empty             |")
         print("|---------------------------------------------------------------------|")
    except ValueError:
      print("|        Please only Enter A, B or C and dont leave empty                   |")


  print("|=============================================================================|")
  if questions.get(key) == user_answer:#This section instructs the code to verify if the user's input matches the dictionary value; if so, the result will be correct; if not, the result will be wrong.
          print("                                          |-------------------------------|     ")
          print("                                          |         Correct!              |     ")  
          print("                                          |-------------------------------|     ")
          score =  score + 1 #< this is so that the total score is displayed in the end.
  else:
          print("                                          |-------------------------------|     ")
          print("                                          |        Incorrect :(           |     ")
          print("                                          |-------------------------------|     ")
 print("| Thanks for taking the quiz; I appreciate you taking the time to do so, and I|\n| hope you learnt something from it.                                          |\n| Your Final Score is:  " + str(score)) #< prints out their total score at the end.







start()
main_menu()
welcome_MCQ_quiz()#< After clicking enter, this function instructs the quiz to direct them straight to welcome_mcq_quiz function.
print("|*****************************************************************************|")
print("|=============================================================================|") 
input("|       Press Enter To Continue To Start Questions...")
play_MCQ_quiz()
print("|=============================================================================|") 


