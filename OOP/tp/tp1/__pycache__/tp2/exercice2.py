# **Exercice 2  **Gestion d'un Système de Réservation de Billets**

class Billet:
    numero: int
    prix: float
    disponible: bool

    def __init__(self, n, p, d):
        self.disponible = d
        self.prix = p
        self.numero = n


class Client:
    nom: str
    prenom: str
    email: str

    def __init__(self, n, p, d):
        self.nom = n
        self.prenom = p
        self.email = d


class Vol:
    numero_vol: int
    destination: str
    date_depart: int
    billets: list

    def __init__(self, n, dd, d, l):
        self.date_depart = dd
        self.destination = d
        self.numero_vol = n
        self.billets = l

    def ajouter_billets(self):
        for bill in self.billets:
            print(f"la billet: {bill} est disponible")

    # @classmethod
    # def numberOfReservation(cls):
    #     return cls.reserved

    # @classmethod
    # def addReservedTicket(cls):
    #     cls.reserved += 1

    def reserver_billets(self, Client):
        for bill in self.billets:
            if bill.disponible:
                bill.disponible = False
                print(
                    f"Billet réservé pour {Client.prenom} {Client.nom} sur le vol {self.numero_vol}")
                return
        print("desole tous les billets sont reserves")

    def afficher_details(self):
        print(
            f"number de vol: {self.numero_vol} destination: {self.destination} date: {self.date_depart}")
        for bill in self.billets:
            if bill.disponible == False:
                print(f"bill {bill.numero} a ete reservee")


class CompagnieAerienne:
    nom: str
    vols: list

    def __init__(self, n, l):
        self.nom = n
        self.vols = l

    def afficher_vols_disponibles(self):
        print(f"Vols disponibles pour la compagnie {self.nom}:")
        for vol in self.vols:
            print(
                f"Vol {vol.numero_vol} - Destination: {vol.destination}, Date de départ: {vol.date_depart}")

    def afficher_details_vol(self, numero_vol):
        for vol in self.vols:
            if vol.numero_vol == numero_vol:
                vol.afficher_details()
                return
        print(f"Vol {numero_vol} non trouvé dans la compagnie {self.nom}")


bill1 = Billet(1111, 50, True)
bill2 = Billet(2222, 50, True)
bill3 = Billet(3333, 50, True)
bill4 = Billet(4444, 50, True)
bill5 = Billet(5555, 50, True)

client1 = Client("nom1", "prenom1", "email1")
client2 = Client("nom2", "prenom2", "email2")

vol1 = Vol(1234, "destination1", 2000, [bill1, bill2, bill3])
vol2 = Vol(5678, "destination2", 2003, [bill4, bill5])

com = CompagnieAerienne("com1", [vol1, vol2])
vol1.reserver_billets(client1)
vol1.afficher_details()
com.afficher_vols_disponibles()
com.afficher_details_vol(5678)
