class KeyError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.text = "you entered the wrong key"

    def __str__(self) -> str:
        return self.text
