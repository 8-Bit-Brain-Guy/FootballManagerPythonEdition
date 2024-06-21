'''
    SpielerGenerator.py
    Pythonskript zur Erzeugung einer Reihe von random Spielern.

    - Lade Vornamens- und Nachnamensliste
    - Generiere zufällige Konfiguration aus Vor- und Nachname
    - Erzeuige Spieler Objekt
    - Weise Spieler Objekt einzelne Vor- Nachnamenkombination zu
    - Generiere für Spieler Objekt Zufalls- Alter, Trainingslevel und Motivation.

'''
import sqlite3
from Spieler import *
from random import *

class Spielergenerator:

    def __init__(self):
        self.spielerListe = list()


    def ladeNamen(self, test = False):
        if test == True:
            self.vornamenListe = ["Lukas", "Ben", "Jonas", "Niklas"]
            self.nachnamenListe = ["Bauer" , "Fischer", "Wegner", "Rüdiger"]
            return

        with open('Vornamenliste.txt') as f:
            self.vornamenListe = f.read()
        with open('Nachnamenliste.txt') as f:
            self.nachnamenListe = f.read()


    def generiereSpieler(self):
        maxSpieler = min(len(self.vornamenListe), len(self.nachnamenListe))
        anz = input("Wieviele Spieler sollen erzeugt werden? Maximal %s sind möglich: " %maxSpieler)
        try:
            anz = int(anz)
        except:
            print("Eingabe \"%s\" ist ungültig." %anz)

        for i in range(int(anz)):
            vn = randrange(0, len(self.vornamenListe))
            nn = randrange(0, len(self.nachnamenListe))
            sp = Spieler(self.vornamenListe[vn], self.nachnamenListe[nn])
            self.spielerListe.append(sp)


    def printe(self):
        for i in range(len(self.spielerListe)):
            print(self.spielerListe[i].__dict__)



# Hauptprogramm
if __name__ == "__main__":
    con = sqlite3.connect("..\FMPE.db")



###     sg = Spielergenerator()
###     sg.ladeNamen(True)
### #    sg.printe()
###     sg.generiereSpieler()
###     sg.printe()