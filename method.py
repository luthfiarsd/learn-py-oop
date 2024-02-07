class Hero:
    heroCount = 0

    def __init__(self, inputName, inputRarity, inputValue) -> None:
        self.name = inputName
        self.rarity = inputRarity
        self.value = inputValue
        Hero.heroCount += 1

    # METHOD VOID TANPA ARGUMEN
    def intro(self):
        print("Hello, my name is " + self.name)

    # METHOD VOID DENGAN ARGUMEN
    def valueUp(self, up):
        self.value += up

    # METHOD DENGAN RETURN
    def getValue(self):
        return self.value


hero1 = Hero("Moskov", "S", 22)
hero2 = Hero("Argus", "A", 18)
hero3 = Hero("Miya", "SS", 25)
hero4 = Hero("Alucard", "B", 15)

hero1.intro()

hero1.valueUp(99)
print(hero2.value)

print(hero1.getValue())
