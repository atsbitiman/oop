class Hero :
    def __init__(self,name,health) :
        self.name = name
        self.health = health

class Hero_int(Hero) :
    def __init__(self,name) :
        #Hero.__init__(self,name,100)
        super().__init__(name,100)

class Hero_strength(Hero) :
    def __init__(self,name) :
        #Hero.__init__(self,name, 200)
        super().__init__(name,200)

lina = Hero_int("lina")
axe = Hero_strength("axe")

print(lina.name, " ", lina.health)
print(axe.name, " ", axe.health)