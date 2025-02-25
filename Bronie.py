class Bron:
    def __init__(self, name, damage, rarity, type,value):
        self.name = name
        self.damage = damage
        self.rarity = rarity
        self.type = type
        self.value = value

bronie_lvl1 =[]  #bronie podstawowe white
bronie_lvl2 =[]  #bronie uncommon green
bronie_lvl3 =[]  #bronie rare blue
bronie_lvl4 =[]  #bronie epic purple
bronie_lvl5 =[]  #bronie legendary yellow

piesci= Bron('Piesci',3,0,"melee",0)
sztylet = Bron('Sztylet',5,1,"melee",5)
krotki_luk = Bron('Krotki Luk',8,2,"ranged",10)
drewniany_miecz = Bron('Drewniany Miecz',4,1,"melee",5)
zelazny_miecz = Bron('Zelazny Miecz',13,2,"melee",10)
miecz_obosieczny = Bron('Miecz Obosieczny',15,3,"melee",30)
topor_wikigna = Bron('Topor Wikigna',15,4,"melee",33)
miecz_samuraja = Bron('Miecz Samuraja',15,5,"melee",50)

bronie_lvl1.extend([sztylet,drewniany_miecz])
bronie_lvl2.extend([krotki_luk,zelazny_miecz])
bronie_lvl3.extend([miecz_obosieczny])
bronie_lvl4.extend([topor_wikigna])
bronie_lvl5.extend([miecz_samuraja])


