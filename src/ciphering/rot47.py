from src.ciphering.rot import Rot


class Rot47(Rot):
    def __init__(self):
        super().__init__(47)

    def shift_char(self, char):
        i = ord(char)
        if 33 <= i <= 126:
            result = chr(33 + (i + (self.shift - 33)) % 94)
            return result
        return char
