class UnsupportedCharacterError(Exception):
    def __init__(self, value = "This text includes a character that is not supported by this algorithm. "):
        self.value = value
        super().__init__(self.value)
