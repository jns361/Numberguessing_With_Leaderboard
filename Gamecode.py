import random
import os
import sys
import time
#print("__file__  =", __file__)
#print("cwd       =", os.getcwd())


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WINNERS_FILE = os.path.join(BASE_DIR, "winners.txt")


#welcome
print("What is your name?")
username = str(input("Name: "))


#path set next to .py file

#function to write
def winnerslist(username, trycount):
    line=f"Name: {username}; Tries: {trycount}\n"
    with open(WINNERS_FILE, "a", encoding="utf-8") as file:
        file.write(line)



#userguess
while True:
    #generating number
    luckynumber = random.randint(1, 100)
    trycount = 0
    print("A random number from 1 to 100 was generated.")
    while True:

        try:
            guess = int(input("Your guess: "))
        except:
            print("That is not a number, try again!")
            continue

        trycount = trycount + 1
        if guess > luckynumber:
            print("Your number is too high.")
            continue
        
        elif guess < luckynumber:
            print("Your number is too low.")
            continue

        elif guess == luckynumber:
            print("You have guessed the correct number!")
            print(f"You needed {trycount} triesto guess correctly. The number was {luckynumber}.")

            #Access function
            winnerslist(username, trycount)

            break

    with open(WINNERS_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()

    #for line in lines:
    #    print(line.strip()) 

    def read_leaderboard(filepath):
        leaderboard = []
        with open(filepath, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if not line:
                    continue  #skip empty lines
                
                parts = line.split(";")
                name_part = parts[0].strip()        
                tries_part = parts[1].strip()       

                #extract names and tries
                name = name_part.split(":", 1)[1].strip()
                
                tries = int(tries_part.split(":", 1)[1].strip())

                leaderboard.append((name, tries))

        #Sort by amount of attempts
        leaderboard.sort(key=lambda x: x[1])
        return leaderboard



    lb = read_leaderboard(WINNERS_FILE)
    print("----- Leaderboard -----")
    for i, (name, tries) in enumerate(lb[:5], start=1):
        print(f"{i}. {name} - {tries} tries")


    #Ask for playing again?
    replay = input("Do you want to play again? (Y/N) ").lower()
    if replay == "y":
        continue
    elif replay == "n":
        print("Thank you for playing!!")
        time.sleep(1)
        sys.exit()

        
