from src.ciphering.rot import Rot


class Rot13(Rot):
    def __init__(self):
        super().__init__(13)

    def shift_char(self, char):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        if char.isalpha():
            result = alphabet[(alphabet.index(char) + self.shift) % 26]
            return result
        return char
