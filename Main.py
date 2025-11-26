Wort = input("Eingabe zu erratendes Wort: ")
Wort = Wort.lower()

# Wort „verstecken“ durch viele neue Zeilen
print("\n" * 50)

print("Du hast 7 Versuche!")


Versuch = 0
ErrateneBuchstaben = ["_"] * len(Wort)
index = 0
HangIndex = 6

HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

while Versuch < 7 and index < len(Wort):

        print("Erraten: ", " ".join(ErrateneBuchstaben))
        Buchstabe = input("Gib einen Buchstaben ein: ")

        if Buchstabe in Wort:
            print(HANGMANPICS[HangIndex])
            print(Buchstabe, "ist richtig")
            print("Du hast noch: ", 7 - Versuch, "Versuche")

            for i in range(len(Wort)):
                if Wort[i] == Buchstabe:
                    if ErrateneBuchstaben[i] == "_":
                     ErrateneBuchstaben[i] = Buchstabe
                     index += 1

        else :
            Versuch = Versuch + 1
            HangIndex = HangIndex -1
            print(HANGMANPICS[HangIndex])
            print(Buchstabe, "ist falsch")
            print("Du hast noch: ", 7 - Versuch, "Versuche")


if index == len(Wort):
    print("Du hast gewonnen!")
else:
    print("Du hast verloren!")

