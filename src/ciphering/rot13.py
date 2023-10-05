from src.ciphering.rot import Rot


class Rot13(Rot):
    def __init__(self):
        super().__init__(13)
