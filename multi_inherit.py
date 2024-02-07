class Team:
    def setTeam(self, teamInput):
        self.team = teamInput

    def showTeam(self):
        return self.team


class Type:
    def setType(self, typeInput):
        self.type = typeInput

    def showType(self):
        return self.type


# SUB CLASS TERDIRI DARI 2 SUPER CLASS
class Hero(Team, Type):
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity


brimstone = Hero("Brim", "SS")

brimstone.setTeam("SENTINEL")
brimstone.setType("DEFENDER")

print("TEAM =>", brimstone.showTeam())
print("TYPE =>", brimstone.showType())

# METHOD RESOLUTION ORDER, MENGURUT PADA YANG DIASSIGN, LALU MENGURUT PADA URUTAN DI DALAM KURUNGNYA, LALU BERULANG SESUAI KONDISI
# DALAM KONTEKS INI YG PERTAMA Hero > Team > Type

# DIAMOND PROBLEM : D > B > C > A
#    A
#  /   \
# B     C
#  \   /
#    D
