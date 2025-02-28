import Bohater
import Bronie as br
import Armor as ar
import random
import Funkcjonalnosci as fn

lista_wrogowt1 = []
lista_wrogowt2 = []
lista_wrogowt3 = []
lista_wrogowt4 = []
lista_wrogowt5 = []

for i in range (1,15):
    lista_wrogowt1.append(fn.tworz_wroga_t1())
    lista_wrogowt2.append(fn.tworz_wroga_t2())
    lista_wrogowt3.append(fn.tworz_wroga_t3())
    lista_wrogowt4.append(fn.tworz_wroga_t4())
    lista_wrogowt5.append(fn.tworz_wroga_t5())

hero = Bohater.MainHero("Macius",100)
count =6
print(f"Witaj {hero.name} otrzymales: \n")
fn.equip_hero(hero)
#
#
#
wrog1 = random.choice(lista_wrogowt1)
fn.atakuj(hero,wrog1)
lista_wrogowt1.remove(wrog1)


# while hero.pokonani_wrogowie < count:
#     fn.atakuj(hero,lista_wrogowt1[0])

    # hero.attack(drugihero)
    # drugihero.attack(hero)
    # hero.wyswietl_ekwipunek()
    # print(f"Wyposazono Maciusia w helm: {hero.helm.name}")
    # print(f"HP maciusia: {hero.health}")
    # print(f"Hp wroga : {drugihero.health}")
    # hero.pasek_hp.rysuj()
    # drugihero.pasek_hp.rysuj()
    # #if drugihero.health <= 70:
    #     # for i in range(0,2):
    #     #     nagroda = random.randrange(1,5)
    #     #     if nagroda == 1:
    #     #          hero.wyposaz_helm(random.choice(ar.helmy_rarity2))
    #     #     elif nagroda == 2:
    #     #         hero.wyposaz_tunike(random.choice(ar.tunika_rarity2))
    #     #     elif nagroda == 3:
    #     #         hero.wyposaz_spodnie(random.choice(ar.spodnie_rarity2))
    #     #     elif nagroda == 4:
    #     #         hero.wyposaz_buty(random.choice(ar.buty_rarity2))
    #     #     elif nagroda == 5:
    #     #         hero.wyposaz_rekawice(random.choice(ar.rekawice_rarity2))
    #     #

