class Hero :
    def __init__(self,name,health) :
        self.name = name
        self.health = health

class Hero_int(Hero) :
    pass
class Hero_strenght(Hero) :
    pass


lina = Hero("lina",10)
print(lina.name)
supri = Hero_int("supri",50)
print(supri.name)