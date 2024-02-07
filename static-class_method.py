class Hero:
    __jumlah = 0

    def __init__(self, value) -> None:
        self.value = value
        Hero.__jumlah += 1

    # METHOD HANYA UNTUK OBJECT
    def getJumlah1(self):
        return Hero.__jumlah

    # METHOD HANYA UNTUK CLASS
    def getJumlah2():
        return Hero.__jumlah

    # METHOD BISA UNTUK OBJECT DAN CLASS

    @staticmethod
    def getJumlah3():
        return Hero.__jumlah

    @classmethod
    def getJumlah4(Cls):
        return Cls.__jumlah


# MASUK PERCOBAAN

chamber = Hero("S")
# print(Hero.getJumlah1())   !!! ERROR
print(chamber.getJumlah1())
omen = Hero("SS")
print(chamber.getJumlah1())
sage = Hero("A")
print(Hero.getJumlah2())
# print(sage.getJumlah2())   !!! ERROR
kayo = Hero("A+")
print(kayo.getJumlah3())
print(kayo.getJumlah4())
