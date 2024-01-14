class TacheInexistante(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.mssg = "un utilisateur tente de marquer comme terminée une tâche qui n'existe pas"

    def __str__(self) -> str:
        return self.mssg
