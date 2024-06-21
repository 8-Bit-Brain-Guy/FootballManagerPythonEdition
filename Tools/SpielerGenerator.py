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
## from Spieler import *
from random import *

####        self.vorname = vn
####        self.nachname = nn
####        self.alter = alter
####        self.gehalt = ge
####        self.spielstaerke = ss


class Spielergenerator:

    def __init__(self):
        self.spielerListe = list()
        self.vornamensListe = list()
        self.nachnamensListe = list()


    def ladeNamen(self, test = False):
        with open('Vornamensliste.txt') as file:
            for line in file:
                self.vornamensListe.append(line.rstrip())
        with open('Nachnamensliste.txt') as file:
            for line in file:
                self.nachnamensListe.append(line.rstrip())


    def generiereSpieler(self):
        vorname = randrange(0, len(self.vornamensListe))
        nachname = randrange(0, len(self.nachnamensListe))
        alter = randrange(20, 60)
        gehalt = round(uniform(50000.0, 1000000.0), 2)
        spielstaerke = 100*random()

        print("Spieler: %s %s, Alter: %d, Gehalt: %f, Spielstärke: %f" %(self.vornamensListe[vorname], self.nachnamensListe[nachname], alter, gehalt, spielstaerke))
        return(self.vornamensListe[vorname], self.nachnamensListe[nachname], alter, gehalt, spielstaerke)


    def speicherSpieler(self):
        return


    def printe(self):
        for i in range(len(self.spielerListe)):
            print(self.spielerListe[i].__dict__)



# Hauptprogramm
if __name__ == "__main__":
    con = sqlite3.connect("..\FMPE.db")
    cur = con.cursor()

    sg = Spielergenerator()
    sg.ladeNamen()
    v,n,a,g,s = sg.generiereSpieler()

    ## res = cur.execute("SELECT name FROM sqlite_master")
    ## INSERT INTO Spieler (Vorname, Nachname, "Alter", Gehalt, Spielstaerke) VALUES ("Mueller", "Mario", 33, 200311.0, 34.44)

    res = cur.execute('INSERT INTO Spieler (Vorname, Nachname, "Alter", Gehalt, Spielstaerke) VALUES ("%s", "%s", %d, %f, %f)' %(v, n, a, g, s))
    con.commit()
    con.close()