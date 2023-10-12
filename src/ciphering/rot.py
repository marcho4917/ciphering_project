class Rot:
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, text):
        text = text.lower()
        result = ""

        for char in text:
            encrypted_char = self.shift_char(char)
            result += encrypted_char
        return result

    def decrypt(self, text):
        return self.encrypt(text)

    def shift_char(self, char):
        raise NotImplementedError('You must implement method "shift_char" in Your ROT class')

