class Erreurnote(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.msg = "nbr should not be negative"

    def __str__(self) -> str:
        return self.msg
