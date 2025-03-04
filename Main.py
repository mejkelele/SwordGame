import Bohater
import Bronie as br
import Armor as ar
import random
import Funkcjonalnosci as fn

# Tworzenie list wrogów
lista_wrogow = {
    1: [fn.tworz_wroga_t1() for i in range(15)],
    2: [fn.tworz_wroga_t2() for i in range(15)],
    3: [fn.tworz_wroga_t3() for i in range(15)],
    4: [fn.tworz_wroga_t4() for i in range(15)],
    5: [fn.tworz_wroga_t5() for i in range(15)]
}

hero = Bohater.MainHero("Macius", 100)
print(f"Witaj {hero.name}, otrzymałeś ekwipunek:\n")
fn.equip_hero(hero)

poziom = 1

while True:
    if not lista_wrogow[poziom]:
        print(f"Pokonałeś wszystkich wrogów na poziomie {poziom}!")
        poziom += 1

    wrog = random.choice(lista_wrogow[poziom])
    print(f"Atakujesz wroga z poziomu {poziom}!")
    fn.atakuj(hero, wrog)
    if wrog.health <= 0:
        lista_wrogow[poziom].remove(wrog)

    if hero.health <= 0:
        print("Twój bohater zginął! Koniec gry.")
        break
