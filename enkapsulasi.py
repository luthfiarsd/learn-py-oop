class Hero:
    def __init__(self, name, health, armor, attack):
        # VARIABEL PRIVATE
        self.__name = name
        self.__health = health
        self.__armor = armor
        self.__attack = attack

    # GETTER, UNTUK MENGELUARKAN VARIABEL PRIVATE HASIL MANIPULASI DARI SETTER
    def getHealth(self):
        return self.__health

    # # SETTER, MEN-SET ATAU MENDEKLARASI VARIABEL PRIVATE
    def attacked(self, lawan):
        self.__health -= lawan.__attack / self.__armor


chamber = Hero("Chamber", 100, 50, 100)
omen = Hero("Omen", 90, 50, 120)

print(chamber.getHealth())
# CHAMBER DISERANG (GOT ATTACKED BY) OLEH OMEN, HEALTH CHAMBER(100)-(ATTACK OMEN(25)/ARMOR CHAMBER(50))
chamber.attacked(omen)
print(chamber.getHealth())
