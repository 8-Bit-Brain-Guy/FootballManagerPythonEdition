'''
    Vereinsgenerator.py
    Pythonskript zur Übertragung der Vereinsdaten aus der Testdatei in die Datenbank.

'''
import sqlite3
## from Spieler import *
from random import *

####        self.vorname = vn
####        self.nachname = nn
####        self.alter = alter
####        self.gehalt = ge
####        self.spielstaerke = ss



con = sqlite3.connect("..\FMPE.db")
cur = con.cursor()

Vereinsliste = list()

with open('Vereinsliste.txt') as file:
    for line in file:
        Vereinsliste.append(line.rstrip())

for v in Vereinsliste:
    res = cur.execute('INSERT INTO Vereine (Name) VALUES ("%s")' %(v))

con.commit()
con.close()




'''
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
        ## res = cur.execute("SELECT name FROM sqlite_master")
        ## INSERT INTO Spieler (Vorname, Nachname, "Alter", Gehalt, Spielstaerke) VALUES ("Mueller", "Mario", 33, 200311.0, 34.44)

        return


    def printe(self):
        for i in range(len(self.spielerListe)):
            print(self.spielerListe[i].__dict__)



# Hauptprogramm
if __name__ == "__main__":

    ## Generiere 100 Spieler

    con = sqlite3.connect("..\FMPE.db")
    cur = con.cursor()
    sg = Spielergenerator()
    sg.ladeNamen()

    for i in range(100):
        v,n,a,g,s = sg.generiereSpieler()
        res = cur.execute('INSERT INTO Spieler (Vorname, Nachname, "Alter", Gehalt, Spielstaerke) VALUES ("%s", "%s", %d, %f, %f)' %(v, n, a, g, s))

    con.commit()
    con.close()

'''