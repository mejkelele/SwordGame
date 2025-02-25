import Bronie as br
import Armor as ar
from PasekHP import PasekHP_terminal
import random


class Bohater:
    def __init__(self, name: str, health):
        self.name = name
        self.health = health
        self.max_health = health
        self.bron = br.piesci
        self.helm = ar.glowa
        self.tunika = ar.tulow
        self.spodnie = ar.nogi
        self.rekawice = ar.dlonie
        self.buty = ar.stopy

    def attack(self, target):
        target.health -= (self.bron.damage - target.wartosc_pancerza())
        target.health = max(target.health, 0)
        target.pasek_hp.update()
        print(
            f"{self.name} zadaje {self.bron.damage - target.wartosc_pancerza()} obrazen przy uzyciu {self.bron.name} dla {target.name} zdrowie wynosi {target.health}")

    def wartosc_pancerza(self):
        wartosc = self.helm.wartosc + self.tunika.wartosc + self.spodnie.wartosc + self.rekawice.wartosc + self.buty.wartosc
        return wartosc

class MainHero(Bohater):
    def __init__(self, name: str, health, bron, helm=None, tunika=None, spodnie=None, rekawice=None, buty=None):
        super().__init__(name, health)
        self.bron = bron
        if helm:
            self.helm = helm
        if tunika:
            self.tunika = tunika
        if spodnie:
            self.spodnie = spodnie
        if rekawice:
            self.rekawice = rekawice
        if buty:
            self.buty = buty
        self.pasek_hp = PasekHP_terminal(self, kolor="green")

    def wyposaz_bron(self, nowaBron):
        self.bron = nowaBron
        print(f"{self.name} wyposazono w  {self.bron.name}")

    def wyposaz_helm(self, nowy_helm):
        self.helm = nowy_helm
        print(f"{self.name} wyposazono w  {self.helm.name}")

    def wyposaz_tunike(self, nowa_tunika):
        self.tunika = nowa_tunika
        print(f"{self.name} wyposazono w  {self.tunika.name}")

    def wyposaz_spodnie(self, nowe_spodnie):
        self.spodnie = nowe_spodnie
        print(f"{self.name} wyposazono w  {self.spodnie.name}")

    def wyposaz_buty(self, nowe_buty):
        self.buty = nowe_buty
        print(f"{self.name} wyposazono w  {self.buty.name}")

    def wyposaz_rekawice(self,nowe_rekawice):
        self.rekawice = nowe_rekawice
        print(f"{self.name} wyposazono w  {self.rekawice.name}")

    def wyrzuc_bron(self):
        self.bron = br.piesci
        print(f"{self.name} wyposazono w  {self.bron.name}")


class MainEnemy(Bohater):
    def __init__(self, name: str, health, bron):
        super().__init__(name, health)
        self.bron = bron
        self.pasek_hp = PasekHP_terminal(self, kolor="blue")



class FirstTierEnemy(Bohater):
    def __init__(self, name: str, health):
        super().__init__(name, health)
        self.bron = random.choice(br.bronie_lvl1)
        self.pasek_hp = PasekHP_terminal(self, kolor="red")



class SecondTierEnemy(Bohater):
    def __init__(self, name: str, health):
        super().__init__(name, health+random.randint(10,25))
        self.bron = random.choice(br.bronie_lvl2)
        self.pasek_hp = PasekHP_terminal(self, kolor="red")


class ThirdTierEnemy(Bohater):
    def __init__(self, name: str, health):
        super().__init__(name, health+random.randint(20,50))
        self.bron = random.choice(br.bronie_lvl3)
        self.pasek_hp = PasekHP_terminal(self, kolor="red")

class FourthTierEnemy(Bohater):
    def __init__(self, name: str, health):
        super().__init__(name, health+random.randint(40,100))
        self.bron = random.choice(br.bronie_lvl4)
        self.pasek_hp = PasekHP_terminal(self, kolor="red")

class FifthTierEnemy(Bohater):
    def __init__(self, name: str, health):
        super().__init__(name, health+random.randint(100,250))
        self.bron = random.choice(br.bronie_lvl5)
        self.pasek_hp = PasekHP_terminal(self, kolor="red")