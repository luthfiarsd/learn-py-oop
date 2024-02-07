class Hero:
    # CLASS VARIABLE
    heroCount = 0

    def __init__(self, inputName, inputRarity, inputValue) -> None:
        # INSTANCE VARIABLE
        self.name = inputName
        self.rarity = inputRarity
        self.value = inputValue
        # MANIPULASI CLASS VARIABLE
        Hero.heroCount += 1


hero1 = Hero("Moskov", "S", 22)
hero2 = Hero("Argus", "A", 18)
hero3 = Hero("Miya", "SS", 25)
hero4 = Hero("Alucard", "B", 15)

print(Hero.heroCount)
