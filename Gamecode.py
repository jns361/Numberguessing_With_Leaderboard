import random
import os
#print("__file__  =", __file__)
#print("cwd       =", os.getcwd())


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WINNERS_FILE = os.path.join(BASE_DIR, "winners.txt")

#generating number
luckynumber = random.randint(1, 100)

#welcome
print("Wie heisst du?")
username = str(input("Name: "))
print("Es wurde eine Zahl zwischen 1 und 100 generiert.")
print("Errätst du sie?")
trycount = 0

#path set next to .py file

#function to write
def winnerslist(username, trycount):
    line=f"Name: {username}; Versuche: {trycount}\n"
    with open(WINNERS_FILE, "a", encoding="utf-8") as file:
        file.write(line)



#userguess
while True:

    try:
        guess = int(input("Dein Tipp:"))
    except:
        print("Das ist keine Zahl! Versuchs nochmal.")
        continue

    trycount = trycount + 1
    if guess > luckynumber:
        print("Deine Zahl ist zu groß.")
        continue
    
    elif guess < luckynumber:
        print("Deine Zahl ist zu niedrig.")
        continue

    elif guess == luckynumber:
        print("Du hast die richtige Zahl erraten!")
        print(f"Du hast {trycount} Versuche gebraucht. Die Zahl war {luckynumber}.")

        #Zugriff auf Funktion
        winnerslist(username, trycount)

        break

with open(WINNERS_FILE, "r", encoding="utf-8") as file:
    lines = file.readlines()

for line in lines:
    print(line.strip()) 

def read_leaderboard(filepath):
    leaderboard = []
    with open(filepath, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if not line:
                continue  # Leere Zeilen überspringen
            # Beispielzeile: "Name: Max; Versuche: 5"
            parts = line.split(";")
            name_part = parts[0].strip()        # "Name: Max"
            tries_part = parts[1].strip()       # "Versuche: 5"

            # Name extrahieren
            name = name_part.split(":", 1)[1].strip()
            # Versuche extrahieren und zu int konvertieren
            tries = int(tries_part.split(":", 1)[1].strip())

            leaderboard.append((name, tries))

    # Sortieren nach Versuchen (Index 1 im Tupel), aufsteigend
    leaderboard.sort(key=lambda x: x[1])
    return leaderboard



# Beispiel: leaderboard ausgeben (Top 5)
lb = read_leaderboard(WINNERS_FILE)
print("----- Leaderboard -----")
for i, (name, tries) in enumerate(lb[:5], start=1):
    print(f"{i}. {name} - {tries} Versuche")

print("→ geschrieben nach:", WINNERS_FILE)