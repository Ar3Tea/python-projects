from random import randint

#create a list of play options
options = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = options[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors? ")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    
    c = input("Do you want to continue?(Y/N) ")
    if c=="Y" or c=="y":
        player = False
    elif c=="N" or c=="n":
        player = True
        print("Thank you for playing!!")
    else:
        print("please enter valid option ")

    print()
    print()
    computer = options[randint(0,2)]