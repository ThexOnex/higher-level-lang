from personne import Personne


def chargeConj(p):
    if p.conjoint == None:
        single.append(p.__str__())
    else:
        married.append(p.__str__())


p1 = Personne("lala", "lala", "F")
p2 = Personne("ben", "ali", "M")
p3 = Personne("pal", "Sara", "F")
p4 = Personne("lolo", "Layla", "M")
p5 = Personne("momo", "Zineb", "F")
single = []
married = []

p1.tazawajBi(p2)
p4.tazawajBi(p3)
p2.tatala9aMin(p1)
chargeConj(p1)
chargeConj(p2)
chargeConj(p3)
chargeConj(p4)
chargeConj(p5)
print("single: ",single)
print("married: ",married)
