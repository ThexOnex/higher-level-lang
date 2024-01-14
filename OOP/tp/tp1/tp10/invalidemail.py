class ValidationError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.mssg = "====l'e-mail est invalide====="

    def __str__(self) -> str:
        return self.mssg
