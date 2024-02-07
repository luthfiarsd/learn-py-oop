class Hero:
    def __init__(self, name, health, armor, strength) -> None:
        self.name = name
        self.health = health
        self.armor = armor
        self.strength = strength

    def serang(self, lawan):
        print(self.name, "menyerang", lawan.name)
        lawan.diserang(self, self.strength)

    def diserang(self, lawan, strengthLawan):
        print(self.name, "diserang", lawan.name)
        attack = strengthLawan / self.armor
        self.health -= attack
        print("Darah berkurang", attack, "\nSisa darah", self.health)


hero1 = Hero("Asep", 100, 20, 15)
hero2 = Hero("Budi", 90, 15, 25)

hero1.serang(hero2)
print()
hero2.serang(hero1)
