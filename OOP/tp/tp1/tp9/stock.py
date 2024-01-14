class StockInsuffisant(Exception):
    def __init__(self, *args: object):
        super().__init__(*args)
        self.mssg = "utilisateur tente d'acheter plus de produits que ceux disponibles en stock ou une quantite indisponible"

    def __str__(self) -> str:
        return self.mssg
