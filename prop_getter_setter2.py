class Mantap:
    def __init__(self, name) -> None:
        self.name = name


chamber = Mantap("apah")
print(chamber.name)

chamber.name = "apaan"
print(chamber.name)
