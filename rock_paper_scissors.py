import random
import sys


print("------------------Welcome to Rock,Papers and Scissors----------------------")
print("\nEnter R or P or S as a choice\n")



def rps(user,computer,user_score,computer_score):

    user = user.upper()
    computer = computer.upper()
    
    if user == computer:
        user_score += 0
        computer_score += 0
        print("Computer entered: {}".format(computer))
        print("User : {}  Computer: {}".format(user_score,computer_score))

    elif user == "P":
        if computer == "S":
            computer_score += 1
        else:
            user_score += 1

        print("Computer entered: {}".format(computer))
        print("User : {}  Computer: {}".format(user_score,computer_score))

    elif user == "S":
        if computer == "R":
            computer_score += 1
        else:
            user_score += 1

        print("Computer entered: {}".format(computer))
        print("User : {}  Computer: {}".format(user_score,computer_score))


    elif user == "R":
        if computer == "P":
            computer_score += 1
        else:
            user_score += 1

        print("Computer entered: {}".format(computer))
        print("User : {}  Computer: {}".format(user_score,computer_score))

    else:
        print("\nInvalid Input")


    return user_score,computer_score

TotalGames = 0
User_Games = 0
Computer_Games = 0
max_score = 5

while True:

    UserScore = 0
    ComputerScore = 0


    while (UserScore < max_score and ComputerScore < max_score):
        user = input("Enter Choice: ")
        computer = random.choice(["R","P","S"])

        UserScore,ComputerScore = rps(user,computer,UserScore,ComputerScore)
        print()

    if UserScore == max_score:
        User_Games += 1
        TotalGames += 1
        print("USer won this game")
    else:
        Computer_Games += 1
        TotalGames += 1
        print("Computer won this game")

    print("\nWould you like to play another game?")
    query = input("Type Yes or No: ").capitalize()

    if query == "No":
        print("\nThank you for playing this game!! \n")
        print("Games won by Users: {}/{}".format(User_Games,TotalGames))
        print("Games won by computer: {}/{}".format(Computer_Games,TotalGames))
        sys.exit()

    elif query == "Yes":
        print("\nGame {}\n".format(TotalGames+1))
        
      
    
    
