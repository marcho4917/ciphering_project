from src.ciphering.rot import Rot


class Rot47(Rot):
    def __init__(self):
        super().__init__(47)

    def encrypt(self, text):
        result = ""
        for i in range(len(text)):
            j = ord(text[i])
            if 33 <= j <= 126:
                result += chr(33 + (j + (self.shift - 33)) % 94)
            else:
                result += text[i]
        return result

