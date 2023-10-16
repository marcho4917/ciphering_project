import pytest
from src.ciphering.rot13 import Rot13


def test_should_return_correct_ciphered_text():
    rot13 = Rot13()
    encrypted_text = rot13.encrypt("mama")
    expected = "znzn"

    assert encrypted_text == expected


def test_should_return_correct_decrypted_text():
    rot13 = Rot13()
    decrypted_text = rot13.decrypt("znzn")
    expected = "mama"

    assert decrypted_text == expected


def test_should_return_correct_shifted_char():
    rot13 = Rot13()
    shifted_char = rot13.shift_char("z")
    expected = "m"

    assert shifted_char == expected


