class ValueError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.mssg = "la chaîne n'est pas dans un format de date valide"

    def __str__(self) -> str:
        return self.mssg
