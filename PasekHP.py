import os


os.system("")

class PasekHP_terminal:
    symbol_pozostale: str="[]"
    symbol_stracone: str="_"
    ogranicznik: str="|"
    kolory: dict = {"red": "\033[91m",
                    "green": "\033[92m",
                    "yellow": "\033[93m",
                    "blue": "\033[94m",}

    def __init__(self,obiekt,dlugosc=20,kolorowy=True,kolor= ""):
        self.obiekt = obiekt
        self.dlugosc = dlugosc
        self.kolorowy = kolorowy
        self.kolor = self.kolory.get(kolor) or self.kolory.get("yellow")
        self.max_warotsc = obiekt.max_health
        self.aktulane_hp = obiekt.health

    def update(self):
        self.aktulane_hp = self.obiekt.health


    def rysuj(self):
        pozostale_zdrowie = round(self.aktulane_hp/self.max_warotsc*self.dlugosc)
        stracone_zdrowie  = self.dlugosc-pozostale_zdrowie
        print(f"{self.obiekt.name} HP: {self.obiekt.health}/{self.obiekt.max_health}")
        print(f"{self.ogranicznik}"
              f"{self.kolor if self.kolorowy else ''}"
              f"{pozostale_zdrowie * self.symbol_pozostale}"
              f"{stracone_zdrowie * self.symbol_stracone}"
              f"{self.kolory['yellow'] if self.kolorowy else ''}"
              f"{self.ogranicznik}")
