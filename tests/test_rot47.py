import pytest
from src.ciphering.rot47 import Rot47


def test_should_return_correct_ciphered_text():
    rot47 = Rot47()
    encrypted_text = rot47.encrypt("mama")
    expected = ">2>2"

    assert encrypted_text == expected


def test_should_return_correct_decrypted_text():
    rot47 = Rot47()
    decrypted_text = rot47.decrypt(">2>2")
    expected = "mama"

    assert decrypted_text == expected


def test_should_return_correct_shifted_char():
    rot47 = Rot47()
    shifted_char = rot47.shift_char("z")
    expected = "K"

    assert shifted_char == expected
