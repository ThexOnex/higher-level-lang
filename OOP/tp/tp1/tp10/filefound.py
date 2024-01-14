class FileNotFoundError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.mssg = "le fichier source n'est pas trouvé"
    def __str__(self) -> str:
        return self.mssg
