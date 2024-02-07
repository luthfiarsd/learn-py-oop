class Hero:
    __countHero = 0

    def __init__(self, name, health, attack, armor) -> None:
        self.__name = name
        self.__healthStd = health
        self.__attackStd = attack
        self.__armorStd = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStd * self.__level
        self.__attackMax = self.__attackStd * self.__level
        self.__armorMax = self.__armorStd * self.__level

        self.__health = self.__healthMax

        Hero.__countHero += 1

    @property
    def info(self):
        return "{}\nHealth   : {}/{}\nAttack   : {}\nArmor    : {}".format(
            self.__name,
            self.__health,
            self.__healthMax,
            self.__attackMax,
            self.__armorMax,
        )


chamber = Hero("Saage", 100, 50, 20)
print(chamber.info)
