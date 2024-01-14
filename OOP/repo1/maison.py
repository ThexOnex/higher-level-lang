class Maison:
    room: str
    adress: str
    prix: float

    def __init__(self, r, k, p):
        self.room = r
        self.adress = k
        self.prix = p

    def __str__(self):
        return f"room: {self.room} kitchen:  {self.adress} price: {self.prix}"
