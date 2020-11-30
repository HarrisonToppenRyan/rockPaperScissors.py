import random

optionsList = ["r", "p", "s"]
compChoiceFinal = None
userChoiceFinal = None 

tie = "You chose the same option was the computer. Draw"
lose = "Your choice was the wrong option. You lose."
win = "Your choice was the right option! You win!"


def user_choice():
    user_choice = input("Choose rock, paper, or scissors (type: r, p, or s): ")
    if user_choice not in optionsList:
        print("Not one of the options. Try again.")
        user_choice()
    elif user_choice == str("r"):
        userChoiceFinal = optionsList[0]
    elif user_choice == str("p"):
        userChoiceFinal = optionsList[1]
    elif user_choice == str("s"):
        userChoiceFinal = optionsList[2]  
    return userChoiceFinal

def computer_choice():
    compChoiceFinal = random.choice(optionsList)
    return compChoiceFinal


def main():
    rockPaperScissors_file = open("rockPaperScissors.txt", "r")
    print(rockPaperScissors_file.read())
    rockPaperScissors_file.close()
    plays = int(input("Best out of how many games?: "))
    player_wins = 0 
    computer_wins = 0 
    while player_wins < plays and computer_wins < plays:
        print("")
        userChoiceFinal = user_choice()
        compChoiceFinal = computer_choice()
        print("")
        endMessage = "Your input: " + str(userChoiceFinal) +  "\nComputer's input: " + str(compChoiceFinal) + "\n"

        if userChoiceFinal == "r":
            if compChoiceFinal == "r":
                print(endMessage + tie)
                print("Scores: \nYou: " + str(player_wins) + " Computer: " + str(computer_wins))
            elif compChoiceFinal == "p":
                computer_wins += 1
                print(endMessage + lose)
                print("Scores: \nYou: " + str(player_wins) + " Computer: " + str(computer_wins))
            elif compChoiceFinal == "s":
                player_wins += 1
                print(endMessage + win)
                print("Scores: \nYou: " + str(player_wins) + " Computer: " + str(computer_wins))

        elif userChoiceFinal == "p":
            if compChoiceFinal == "r":
                player_wins += 1
                print(endMessage + win)
                print("Scores: \nYou: " + str(player_wins) + " Computer: " + str(computer_wins))
            elif compChoiceFinal == "p":
                print(endMessage + tie)
                print("Scores: \nYou: " + str(player_wins) + " Computer: " + str(computer_wins))
            elif compChoiceFinal == "s":
                computer_wins += 1
                print(endMessage + lose)
                print("Scores: \nYou: " + str(player_wins) + " Computer: " + str(computer_wins))

        elif userChoiceFinal == "s":
            if compChoiceFinal == "r":
                computer_wins += 1
                print(endMessage + lose)
                print("Scores: \nYou: " + str(player_wins) + " Computer: " + str(computer_wins))
            elif compChoiceFinal == "p":
                player_wins += 1
                print(endMessage + win)
                print("Scores: \nYou: " + str(player_wins) + " Computer: " + str(computer_wins))
            elif compChoiceFinal == "s":
                print(endMessage + tie)
                print("Scores: \nYou: " + str(player_wins) + " Computer: " + str(computer_wins))
                
        if player_wins == plays or computer_wins == plays:
            print("Scores: \nYou: " + str(player_wins) + " Computer: " + str(computer_wins))
            print("We have a winner!")
            break
main()