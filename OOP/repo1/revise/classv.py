class Var:
    variable = 33
    numberOfVars = 0

    def __init__(self, n: str, l: str, a: int) -> None:
        self.name = n
        self.lastName = l
        self.age = a
        Var.numberOfVars += 1

    @classmethod
    def TheStat(cls):
        return cls.variable

    def fullname(self):
        return self.name+" "+self.lastName


vari = Var("Sara", "Last name", 18)
# # print(vari.fullname())
# # print(vari.__dict__)
# vari2 = Var("2", "l 2", 22)
# print(Var.numberOfVars)

# vari3 = Var("3", "l 3", 33)
# print(Var.numberOfVars)
print(vari.TheStat())
