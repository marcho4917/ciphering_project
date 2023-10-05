class Rot:
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, text):
        text = text.lower()
        result = ""
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        # Replace each letter in the string with a letter which is self.shift positions further
        for char in text:
            if char.isalpha():
                result += alphabet[(alphabet.index(char) + self.shift) % 26]
            else:
                result += char
        return result

    def decrypt(self, text):
        return self.encrypt(text)
