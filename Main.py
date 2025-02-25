import Bohater
import Bronie as br
import Armor as ar
import random

hero = Bohater.MainHero("Macius",100,br.sztylet,random.choice(ar.helmy_rarity4))
drugihero =  (Bohater.FirstTierEnemy("WrogMaciusia",100))
# trzeba podzelic helmy na listy na poziomie rarity 
#poczatek opis twojego bohtaera
while True:
    hero.attack(drugihero)
    drugihero.attack(hero)
    print(f"Wyposazono Maciusia w helm: {hero.helm.name}")
    print(f"HP maciusia: {hero.health}")
    print(f"Hp wroga : {drugihero.health}")
    hero.pasek_hp.rysuj()
    drugihero.pasek_hp.rysuj()
    #if drugihero.health <= 70:
        # for i in range(0,2):
        #     nagroda = random.randrange(1,5)
        #     if nagroda == 1:
        #          hero.wyposaz_helm(random.choice(ar.helmy_rarity2))
        #     elif nagroda == 2:
        #         hero.wyposaz_tunike(random.choice(ar.tunika_rarity2))
        #     elif nagroda == 3:
        #         hero.wyposaz_spodnie(random.choice(ar.spodnie_rarity2))
        #     elif nagroda == 4:
        #         hero.wyposaz_buty(random.choice(ar.buty_rarity2))
        #     elif nagroda == 5:
        #         hero.wyposaz_rekawice(random.choice(ar.rekawice_rarity2))
        #



    input()