class Hero:
    def __init__(self, name, health) -> None:
        self.name = name
        self.health = health

    def showInfo(self):
        print("{} with health : {}".format(self.name, self.health))


class Hero_sentinel(Hero):
    def __init__(self, name, health) -> None:
        super().__init__(name, health)
        # SAMA DENGAN =>  Hero.__init__(self, name, health)
        super().showInfo()
        # SAMA DENGAN =>  Hero.showInfo(self)


class Hero_duelist(Hero):
    def __init__(self, name, health) -> None:
        super().__init__(name, health)
        # SAMA DENGAN =>  Hero.__init__(self, name, health)
        super().showInfo()
        # SAMA DENGAN =>  Hero.showInfo(self)


chamber = Hero_sentinel("Chamber", 100)
phoenix = Hero_duelist("Phoenix", 120)
