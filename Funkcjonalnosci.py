import Armor
import Bronie
import Bohater
import random
import time

def losuj_helmt1():
    return random.choice(Armor.helmy_rarity1)

def losuj_helmt2():
    return random.choice(Armor.helmy_rarity2)

def losuj_helmt3():
    return random.choice(Armor.helmy_rarity3)

def losuj_helmt4():
    return random.choice(Armor.helmy_rarity4)

def losuj_helmt5():
    return random.choice(Armor.helmy_rarity5)

def losuj_tunikat1():
    return random.choice(Armor.tunika_rarity1)

def losuj_tunikat2():
    return random.choice(Armor.tunika_rarity2)

def losuj_tunikat3():
    return random.choice(Armor.tunika_rarity3)

def losuj_tunikat4():
    return random.choice(Armor.tunika_rarity4)

def losuj_tunikat5():
    return random.choice(Armor.tunika_rarity5)

def losuj_spodniet1():
    return random.choice(Armor.spodnie_rarity1)

def losuj_spodniet2():
    return random.choice(Armor.spodnie_rarity2)

def losuj_spodniet3():
    return random.choice(Armor.spodnie_rarity3)

def losuj_spodniet4():
    return random.choice(Armor.spodnie_rarity4)

def losuj_spodniet5():
    return random.choice(Armor.spodnie_rarity5)

def losuj_rekawicet1():
    return random.choice(Armor.rekawice_rarity1)

def losuj_rekawicet2():
    return random.choice(Armor.rekawice_rarity2)

def losuj_rekawicet3():
    return random.choice(Armor.rekawice_rarity3)

def losuj_rekawicet4():
    return random.choice(Armor.rekawice_rarity4)

def losuj_rekawicet5():
    return random.choice(Armor.rekawice_rarity5)
def losuj_butyt1():
    return random.choice(Armor.buty_rarity1)

def losuj_butyt2():
    return random.choice(Armor.buty_rarity2)

def losuj_butyt3():
    return random.choice(Armor.buty_rarity3)

def losuj_butyt4():
    return random.choice(Armor.buty_rarity4)

def losuj_butyt5():
    return random.choice(Armor.buty_rarity5)

def losuj_bront1():
    return random.choice(Bronie.bronie_lvl1)

def losuj_bront2():
    return random.choice(Bronie.bronie_lvl2)

def losuj_bront3():
    return random.choice(Bronie.bronie_lvl3)

def losuj_bront4():
    return random.choice(Bronie.bronie_lvl4)


def losuj_bront5():
    return random.choice(Bronie.bronie_lvl5)


def equip_hero(hero):
    hero.wyposaz_helm(losuj_helmt1())
    hero.wyposaz_tunike(losuj_tunikat1())
    hero.wyposaz_spodnie(losuj_spodniet1())
    hero.wyposaz_buty(losuj_butyt1())
    hero.wyposaz_rekawice(losuj_rekawicet1())
    hero.wyposaz_bron(losuj_bront2())

def atakuj(hero,target):
    while hero.health > 0 and target.health > 0:
        hero.attack(target)
        target.attack(hero)
        print("\n")
        time.sleep(1)
    if hero.health > 0 and target.health <= 0:
        hero.pokonani_wrogowie +=1
        print(f"Koniec walki! Wygrał {hero.name }.")
    else:
        return 0



def tworz_wroga_t1():
    return Bohater.FirstTierEnemy(random.choice(Bohater.enemies),random.randint(80,110))

def tworz_wroga_t2():
    return Bohater.SecondTierEnemy(random.choice(Bohater.enemies),random.randint(80,110))
def tworz_wroga_t3():
    return Bohater.SecondTierEnemy(random.choice(Bohater.enemies),random.randint(80,110))
def tworz_wroga_t4():
    return Bohater.SecondTierEnemy(random.choice(Bohater.enemies),random.randint(80,110))
def tworz_wroga_t5():
    return Bohater.SecondTierEnemy(random.choice(Bohater.enemies),random.randint(80,110))

def wygrana_tier2():
    lista_list = [Armor.helmy_rarity2,Armor.buty_rarity2,Armor.rekawice_rarity2,Armor.spodnie_rarity2,Armor.tunika_rarity2]
    prize_t2 =random.choice(random.choice(lista_list))
    return prize_t2
