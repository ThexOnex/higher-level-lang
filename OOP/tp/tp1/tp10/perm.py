class PermissionError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.mssg = "l'utilisateur n'a pas la permission d'écrire dans le fichier de destination"
    def __str__(self) -> str:
        return self.mssg
