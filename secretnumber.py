
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
currenttry = 1

while guess != secret and currenttry <= maxtry:
    print("Das ist ihr " + str(currenttry) + " Versuch von " + str(maxtry) + " Versuchen.")
    guess = int(raw_input("Geben Sie Ihren Vorschlag für die gesuchte Zahl ein: "))
    if guess != secret:
        currenttry += 1  # selber wie 'currentry = currenttry + 1'
        print("Leider falsch! Sie haben die gesuchte Zahl nicht erraten.")
    else:
        print("Volltreffer! Sie haben die gesuchte Zahl gefunden!")

if guess != secret:
    print "Sie haben die maximale Anzahl an Versuchen aufgebraucht."