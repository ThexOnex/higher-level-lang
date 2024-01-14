class AgeInvalide(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.mssg = "l'âge n'est pas un nombre positif"
    def __str__(self) -> str:
        return self.mssg
