import os
import random

#function to play again
def again():
    inpAgain = input('''Do you want to play again?
Y or y for Yes
N or n for No ''')
    if(inpAgain.upper() == "Y"):
        os.system("cls")
        print("Ok, here we go!\n")
        play()
    elif(inpAgain.upper() == "N"):
        print("See you soon!")
    else:
        again()

#function to play
def play():
    player = input('''\'r\' for Rock
\'p\' for Paper
\'s\' for Scissors
Choose: 
''')
    computer = random.choice(["r", "p", "s"])
    
    if(player.upper() == computer.upper()):
        print("\n==Tie==\n")
    elif(player_win(player.upper(), computer.upper()) == True):
        print("You Won\n")
    else:
        print("You lost!\n")

#function to check if the player won   
def player_win(player, computer):
    if(player == "R" and computer == "S") or (player == "S" and computer == "P") or (player == "P" and computer == "R"):
        return True

play()