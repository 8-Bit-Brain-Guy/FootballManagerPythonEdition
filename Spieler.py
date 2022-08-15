class Spieler:
    _count = 0
    
    def __init__(self, vn, nn, alter = None, tr = None, mo = None):
        # print("Constructor of Player class called...")
        Spieler._count += 1
        
        self.vorname = vn
        self.nachname = nn
        self.alter = alter
        self.trainiertheit = tr
        self.motiviertheit = mo


    def printeAttribute(self):
        print(self.vorname, self.nachname, self.alter, self.trainiertheit, self.motiviertheit)
        print(self.__dict__)