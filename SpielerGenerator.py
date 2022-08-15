'''
    SpielerGenerator.py
    Pythonskript zur Erzeugung einer Reihe von random Spielern.

    - Lade Vornamens- und Nachnamensliste
    - Generiere zufällige Konfiguration aus Vor- und Nachname
    - Erzeuige Spieler Objekt    
    - Weise Spieler Objekt einzelne Vor- Nachnamenkombination zu
    - Generiere für Spieler Objekt Zufalls- Alter, Trainingslevel und Motivation.
    
'''

from Spieler import *
vornameListe = ["A", "B", "C"]
nachnamenListe = ["X", "Y", "Z"]

maxSpieler = min(len(vornameListe), len(nachnamenListe))
anz = input("Wieviele Spieler sollen erzeugt werden? Maximal %s sind möglich: " %maxSpieler)
try:
    anz = int(anz)
except:
    print("Eingabe \"%s\" ist ungültig." %anz)


for i in range(int(anz)):
    sp = Spieler()
    print(i)


