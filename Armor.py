
#body slots
#1 glowa
#2 tulow
#3 spodnie
#4 rekawice
#5 buty
class Pancerz:
    def __init__(self,name,rarity,wartosc=0):
        self.name = name
        self.wartosc = wartosc
        self.rarity = rarity



#class Procentowy(Pancerz):
#   def __init__(self,name,wartosc,rarity,):
#        super().__init__() ijkk



class Helm(Pancerz):
    bodyslot = 1
    def __init__(self,name,rarity,wartosc=0):
        super().__init__(name,rarity,wartosc)


class Tunika(Pancerz):
    bodyslot = 2
    def __init__(self,name,rarity,wartosc=0):
        super().__init__(name,rarity,wartosc)



class Spodnie(Pancerz):
    bodyslot = 3
    def __init__(self,name,rarity,wartosc=0):
        super().__init__(name,rarity,wartosc)



class Rekawice(Pancerz):
    bodyslot = 4
    def __init__(self,name,rarity,wartosc=0):
        super().__init__(name,rarity,wartosc)
        bodyslot = 4


class Buty(Pancerz):
    bodyslot = 5
    def __init__(self,name,rarity,wartosc=0):
        super().__init__(name,rarity,wartosc)


glowa = Helm("glowa",0,0)
tulow = Tunika("tulow",0,0)
nogi = Spodnie("nogi",0,0)
stopy = Buty("stopy",0,0)
dlonie = Rekawice("dlonie",0,0)
helmy_rarity1 =[
    Helm("Skórzany Kask", 1, 2),
    Helm("Zardzewialy Hełm", 1, 5),
    Helm("Znoszony Kaptur", 1, 1),
    Helm("Zepsuty Hełm", 1, 4),
    Helm("Czapka", 1, 2),]
helmy_rarity2 = [
    Helm("Żelazny Hełm", 2, 10),
    Helm("Rogaty Hełm", 2, 12),
    Helm("Ulepszony Kaptur", 2, 8),
    Helm("Wzmocniony Hełm", 2, 15),
    Helm("Armet", 2, 9),]
helmy_rarity3 = [
    Helm("Hełm Rycerski", 3, 20),
    Helm("Kaptur Krzyżowca", 3, 21),
    Helm("Hełm Bitewny", 3, 28),
    Helm("Świątynny Hełm", 3, 30),
    Helm("Żelazna Maska", 3, 29),]
helmy_rarity4 = [
    Helm("Smoczy Hełm", 4, 56),
    Helm("Hełm Przywódcy", 4, 61),
    Helm("Czaszka Demona", 4, 70),
    Helm("Hełm Rycerza Cienia", 4, 78),
    Helm("Hełm Gryfona", 4, 65)]
helmy_rarity5 = [
    Helm("Niebiańska Korona", 5, 148),
    Helm("Hełm Feniksa", 5, 130),
    Helm("Piekielny Hełm", 5, 160),
    Helm("Hełm Tytana", 5, 155),
    Helm("Hełm Pustki", 5, 167)]
spodnie_rarity1 = [
    Spodnie("Skórzane Spodnie",1,3),
    Spodnie("Brudne Łachmany",1,1),
    Spodnie("Znoszone Spodnie",1,4),
    Spodnie("Dziurawe Spodnie",1,3),
    Spodnie("Kalesony",1,2)]
spodnie_rarity2 = [Spodnie("Płytowe Nogawice",2,9),
    Spodnie("Wzmocnione Spodnie", 2, 10),
    Spodnie("Nogawice Myśliwego", 2, 8),
    Spodnie("Skórzane Nogawice", 2, 7),
    Spodnie("Spodnie Wędrowca", 2, 6),
]
spodnie_rarity3 = [
    Spodnie("Rycerskie Nogawice", 3, 22),
    Spodnie("Bitewne Spodnie", 3, 24),
    Spodnie("Zbrojne Nogawice", 3, 26),
    Spodnie("Gwardyjskie Spodnie", 3, 28),
    Spodnie("Świątynne Nogawice", 3, 29),
]
spodnie_rarity4 = [
    Spodnie("Smocze Nogawice", 4, 58),
    Spodnie("Nogawice Przywódcy", 4, 62),
    Spodnie("Cieniste Nogawice", 4, 69),
    Spodnie("Pancerne Nogawice", 4, 75),
    Spodnie("Nogawice Gryfona", 4, 66),
]
spodnie_rarity5 = [
    Spodnie("Piekielne Nogawice", 5, 140),
    Spodnie("Nogawice Feniksa", 5, 133),
    Spodnie("Tytaniczne Nogawice", 5, 155),
    Spodnie("Niebiańskie Nogawice", 5, 150),
    Spodnie("Nogawice Pustki", 5, 170),
]
tunika_rarity1 = [
    Tunika("Lniana Tunika", 1, 3),
    Tunika("Podarta Koszula", 1, 2),
    Tunika("Szmaciana Tunika", 1, 4),
    Tunika("Znoszona Tunika", 1, 3),
    Tunika("Prosta Koszula", 1, 2),
]
tunika_rarity2 = [
    Tunika("Kolczuga", 2, 12),
    Tunika("Wzmocniona Tunika", 2, 10),
    Tunika("Skórzana Kamizelka", 2, 8),
    Tunika("Szata Wędrowca", 2, 6),
    Tunika("Pancerna Tunika", 2, 9),
]
tunika_rarity3 = [
    Tunika("Rycerska Zbroja", 3, 24),
    Tunika("Bitewna Kolczuga", 3, 28),
    Tunika("Gwardyjska Szata", 3, 26),
    Tunika("Świątynne Szaty", 3, 30),
    Tunika("Pancerz Krzyżowca", 3, 29),
]
tunika_rarity4 = [
    Tunika("Smocza Zbroja", 4, 60),
    Tunika("Zbroja Przywódcy", 4, 65),
    Tunika("Zbroja Cienia", 4, 72),
    Tunika("Pancerz Gryfona", 4, 70),
    Tunika("Zbroja Demona", 4, 78),
]
tunika_rarity5 = [
    Tunika("Piekielna Zbroja", 5, 150),
    Tunika("Zbroja Feniksa", 5, 135),
    Tunika("Tytaniczny Pancerz", 5, 160),
    Tunika("Niebiańska Zbroja", 5, 155),
    Tunika("Pancerz Pustki", 5, 175),
]
rekawice_rarity1 = [
    Rekawice("Skórzane Rękawice", 1, 2),
    Rekawice("Przetarte Rękawice", 1, 1),
    Rekawice("Znoszone Rękawice", 1, 3),
    Rekawice("Stare Rękawice", 1, 2),
    Rekawice("Szmaciane Rękawice", 1, 1),
]
rekawice_rarity2 = [
    Rekawice("Wzmocnione Rękawice", 2, 8),
    Rekawice("Kolcze Rękawice", 2, 10),
    Rekawice("Skórzane Rękawice Myśliwego", 2, 7),
    Rekawice("Metalowe Rękawice", 2, 9),
    Rekawice("Zbrojne Rękawice", 2, 11),
]
rekawice_rarity3 = [
    Rekawice("Rycerskie Rękawice", 3, 18),
    Rekawice("Bitewne Rękawice", 3, 20),
    Rekawice("Gwardyjskie Rękawice", 3, 22),
    Rekawice("Świątynne Rękawice", 3, 24),
    Rekawice("Pancerne Rękawice", 3, 26),
]
rekawice_rarity4 = [
    Rekawice("Smocze Rękawice", 4, 48),
    Rekawice("Rękawice Przywódcy", 4, 52),
    Rekawice("Cieniste Rękawice", 4, 55),
    Rekawice("Zbrojne Rękawice", 4, 58),
    Rekawice("Rękawice Gryfona", 4, 50),
]
rekawice_rarity5 = [
    Rekawice("Piekielne Rękawice", 5, 120),
    Rekawice("Rękawice Feniksa", 5, 110),
    Rekawice("Tytaniczne Rękawice", 5, 130),
    Rekawice("Niebiańskie Rękawice", 5, 125),
    Rekawice("Rękawice Pustki", 5, 140),
]
buty_rarity1 = [
    Buty("Skórzane Buty", 1, 2),
    Buty("Zniszczone Buty", 1, 1),
    Buty("Dziurawe Trzewiki", 1, 3),
    Buty("Szmaciane Buty", 1, 2),
    Buty("Wytarte Sandały", 1, 1),
]
buty_rarity2 = [
    Buty("Wzmocnione Buty", 2, 8),
    Buty("Pancerne Buty", 2, 10),
    Buty("Skórzane Buty Myśliwego", 2, 7),
    Buty("Kolcze Buty", 2, 9),
    Buty("Trzewiki Wojownika", 2, 11),
]
buty_rarity3 = [
    Buty("Rycerskie Buty", 3, 18),
    Buty("Bitewne Buty", 3, 20),
    Buty("Gwardyjskie Buty", 3, 22),
    Buty("Świątynne Buty", 3, 24),
    Buty("Pancerne Buty", 3, 26),
]
buty_rarity4 = [
    Buty("Smocze Buty", 4, 48),
    Buty("Buty Przywódcy", 4, 52),
    Buty("Cieniste Buty", 4, 55),
    Buty("Zbrojne Buty", 4, 58),
    Buty("Buty Gryfona", 4, 50),
]
buty_rarity5 = [
    Buty("Piekielne Buty", 5, 120),
    Buty("Buty Feniksa", 5, 110),
    Buty("Tytaniczne Buty", 5, 130),
    Buty("Niebiańskie Buty", 5, 125),
    Buty("Buty Pustki", 5, 140),
]



