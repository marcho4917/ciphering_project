import pytest
from src.inputs.input_reader import InputReader


def test_get_user_input_with_valid_input_should_return_user_input(mocker):
    mocker.patch("builtins.input", return_value="sun")
    result = InputReader.get_user_input(message_to_user="")

    assert result == "sun"


def test_get_user_input_with_invalid_input_should_return_warning(mocker, capsys):
    mocker.patch("builtins.input", return_value="kłębek")
    InputReader.get_user_input(message_to_user="")
    captured = capsys.readouterr()
    expected = "Don't use polish characters\n"

    assert captured.out == expected



