import Bohater
import Bronie as br
import Armor as ar
import random
import Funkcjonalnosci as fn

hero = Bohater.MainHero("Macius",100)
drugihero =  (Bohater.ThirdTierEnemy("WrogMaciusia",100))
count =6
print(f"Witaj {hero.name} otrzymales: \n")
fn.equip_hero(hero)

while hero.pokonani_wrogowie < count:
    fn.atakuj(hero,drugihero)

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



    input()