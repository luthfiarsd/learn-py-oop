# SUPER CLASS
class Hero:
    __jumlah = 0

    def __init__(self, health, value) -> None:
        self.__health = health
        self.__value = value

    @property
    def info(self):
        return "Health : {}\nValue  : {}".format(self.__health, self.__value)


# SUB CLASS, MEWARISKAN DARI SUPER CLASS
class Hero_sentinel(Hero):
    pass


class Hero_duelist(Hero):
    pass


chamber = Hero_sentinel(100, "SS")
phoenix = Hero_duelist(120, "SS+")

print("CHAMBER\n" + chamber.info)
print("PHOENIX\n" + phoenix.info)
