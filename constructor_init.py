class Hero:
    def __init__(self, inputName, inputRarity) -> None:
        self.name = inputName
        self.rarity = inputRarity


hero1 = Hero("mantap", 22)

print(hero1.name)
print(hero1.rarity)
print(hero1.__dict__)
