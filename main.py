def play_MCQ_quiz():
  print("Hello, Welcome to my multi choice quiz made 2022 \n please type in your name and read the rules,\n please note this quiz was entitled to help year 11 students so if you are trying this quiz below year 11 dont be dishearten if the results arent upto your excepations, thanks and enjoy!")






def main_menu():
    print("|*******************************|")
    print("| HELLO! |")
    print("WELCOME TO MY MATHS QUIZ        |")
    print("|*******************************|")
    print("| Please select an option:      |")
    print("|*                             *|")
    print("| 1. Play Math quiz             |")
    print("| 2. Know the rules             |")
    print("| 3. Quit                       |")
    print("|*******************************|")
    choice = input("| Enter 1, 2, or 3: ")

    if choice == "1":
        play_MCQ_quiz()
    elif choice == "2":
        print("| These are the rules!  |")
        print("| 1. No cheating                |")
        print("| 2. only calculators are allowed    |")
        print("| 3. Do Not Get Mad Instead Have Fun!!                 |")
    elif choice == "3":
        print("|Hope you had fun :) !|")
        print("|Thanks for playing and hope you have a great day|")
        quit()
    


main_menu()
