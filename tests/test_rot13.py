import pytest
from src.ciphering.rot13 import Rot13


def test_should_return_correct_ciphered_text():
    rot13 = Rot13()
    encrypted_text = rot13.encrypt("mama")
    expected = "znzn"

    assert encrypted_text == expected


def test_should_return_correct_encrypted_text():
    rot13 = Rot13()
    decrypted_text = rot13.decrypt("znzn")
    expected = "mama"

    assert decrypted_text == expected

