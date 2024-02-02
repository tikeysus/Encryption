class UnsupportedCharacterError(Exception):
    def __init__(self, value = "This text includes a character that is not supported by this algorithm. "):
        self.value = value
        super().__init__(self.value)

class BadKeyLengthError(Exception):
    def __init__(self, value = "Please modify the key so that it is at least as long as the plaintext. "):
        self.value = value
        super().__init__(self.value)