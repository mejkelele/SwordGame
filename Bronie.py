class Bron:
    def __init__(self, name, damage, rarity, type,value):
        self.name = name
        self.damage = damage
        self.rarity = rarity
        self.type = type
        self.value = value

bronie_lvl1 =[
    Bron('Sztylet',5,1,"melee",5),
    Bron('Drewniany Miecz',4,1,"melee",5)]  #bronie podstawowe white
bronie_lvl2 =[
    Bron('Krotki Luk',8,2,"ranged",10),
    Bron('Zelazny Miecz',13,2,"melee",10)
]  #bronie uncommon green
bronie_lvl3 =[
    Bron('Miecz Obosieczny',15,3,"melee",30)
]  #bronie rare blue
bronie_lvl4 =[
    Bron('Topor Wikigna',15,4,"melee",33)
]  #bronie epic purple
bronie_lvl5 =[
    Bron('Miecz Samuraja',15,5,"melee",50)
]  #bronie legendary yellow

piesci= Bron('Piesci',3,0,"melee",0)


