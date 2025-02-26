import Bohater
import Bronie as br
import Armor as ar
import random

hero = Bohater.MainHero("Macius",100,br.sztylet,)
first_enemy =  (Bohater.FirstTierEnemy("WrogMaciusia",100))
#poczatek opis twojego bohtaera
print(f"Twoja walka zaczyna się tutaj. Witaj {hero.name} \n"
      f"Atakujesz {first_enemy.name}")
while True:

    hero.attack(first_enemy)
    first_enemy.attack(hero)
    hero.pasek_hp.rysuj()
    first_enemy.pasek_hp.rysuj()
    if first_enemy.health <= 0:
        print(f"Pokonano {first_enemy.name}\n")

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