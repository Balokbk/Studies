import random
import os

#function to use a dice
def dices():
    print("\n=========Dice=========\n")
    n = input('''What dice do you want to use?
Recommendations: 4, 6, 8, 12, 20, 100
(You can use any dice you like!) 
''')
    if n.isdigit():
        rngDice = random.randint(1, int(n))
        print(f"\nYou got {rngDice} in a {n} dice.")
        print("\n======================\n")
    else:
        os.system("cls")
        print("[ERROR] Insert a Number please! ")
        dices()

#functon to get the name of the characters
def inName():
    name = input("Insert the name of the char: ")
    if name == "" or name == " ":
        os.system("cls")
        inName()
    else:
        row.append(name)

#function to remove a name from the row
def remove():
    if len(row) == 0:
        os.system("cls")
        print("You don't have any characters in the row!\n")
        choice()

    rmName = input(f'''Here your row:
{row}
Choose who do you want to remove(insert the name, 'exit' to get back to the menu):
''')
    if rmName in row:
        os.system("cls")
        n = row.index(rmName)
        del row[n]
        remove()
    elif rmName.upper() == "EXIT":
        os.system("cls")
        choice()
    else:
        os.system("cls")
        print("[ERROR]This name doesn't exist in the row!\n")
        remove()

#function to check and show the row
def isRow():
    if len(row) != 0:
        i = int(0)
        while i < len(row):
            print(f'''{int(i) + 1}° - {row[i]}
-----------''')
            i += 1 

#the main part
def choice():
    isRow()
    c = input('''Choose what do you want to do: 
1- New_char 
2- Remove_char 
3- Dice_roller
#- Exit 
''')

    match c:
        case "1":
            os.system("cls")
            inName()
            print(f"Now {row} is saved!\n")
        case "2":
            os.system("cls")
            remove()
        case "3":
            os.system("cls")
            dices()
        case "#":
            os.system("cls")
            os.abort()
    choice()

row = []
choice()
