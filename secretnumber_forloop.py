
#-*- coding: utf-8 -*-
import random

# GUESS THE SECRET NUMBERS

# Varibles:
maxtry = 3
a = 1
b = 9
secret = random.randint(a,b)

# Leerzeichen entfernen: .strip() am Ende von einem String z.B. raw_input("Testeingabe ohne Abstand dank strip").strip()

# for-loop: über einen definierten Bereich läuft die schleife
# while-loop: laufen so lange bis eine Bedingung erfüllt ist

# The Game:
guess = None

for i in range(3):
    print("Das ist ihr " + str(i+1) + " Versuch von " + str(maxtry) + " Versuchen.")
    guess = int(raw_input("Geben Sie Ihren Vorschlag für die gesuchte Zahl ein: "))
    if guess != secret:
        print("Leider falsch! Sie haben die gesuchte Zahl nicht erraten.")
    else:
        print("Volltreffer! Sie haben die gesuchte Zahl gefunden!")
        break
print("Sie haben die maximale Anzahl an Versuchen aufgebraucht. Das Spiel ist zu Ende!")