import pytest
from src.menu import menu


expected_menu = ('1. Encrypt plain text (ROT47/ ROT13)\n'
                 '2. Save encrypted text to file\n'
                 '3. Decrypt encrypted text from file\n'
                 '4. Print encrypted words stored in memory\n'
                 '5. Exit\n')


@pytest.fixture
def get_menu_mock():
    return menu.Menu()


@pytest.fixture
def set_show_menu_mock(mocker):
    mock_show_menu = mocker.patch("src.menu.menu.Menu.show_menu", return_value=expected_menu)
    return mock_show_menu


def test_show_menu_and_input_1(mocker, get_menu_mock, set_show_menu_mock):
    menu_mock = get_menu_mock
    tested_inputs = ["1", "mama", "rot13"]
    mocker.patch('builtins.input', side_effect=tested_inputs)
    menu_mock.show_menu()

    set_show_menu_mock.assert_called_once()


def test_show_menu_and_input_2(mocker, get_menu_mock, set_show_menu_mock):
    menu_mock = get_menu_mock
    menu_mock.encrypted_text = "mama"
    menu_mock.text_dict = {"rot13": "znzn"}
    tested_inputs = ["2", "tested_filename"]
    mocker.patch('builtins.input', side_effect=tested_inputs)
    menu_mock.show_menu()

    set_mock_save_to_file = mocker.patch("src.files.file_handler.FileHandler.save_to_file")

    set_mock_save_to_file.called_once_with("tested_filename", menu_mock.text_dict)
    set_show_menu_mock.assert_called_once()


def test_show_menu_and_input_3(mocker, get_menu_mock, capsys):
    tested_inputs = ["3", "file_name", "5"]
    mocker.patch("builtins.input", side_effect=tested_inputs)
    mocker.patch("src.files.file_handler.FileHandler.read_from_file", return_value={"rot13": 'znzn'})
    menu_mock = get_menu_mock
    expected = (expected_menu +
                "Your text after decrypt it is: mama\n" +
                expected_menu +
                "Goodbye!\n")

    menu_mock.show_menu()

    captured = capsys.readouterr()
    assert captured.out == expected


def test_show_menu_and_input_4(mocker, capsys, get_menu_mock):
    tested_inputs = ["4", "5"]
    menu_mock = get_menu_mock
    mocker.patch.object(menu_mock, "text_dict", {"rot13": "znzn", "rot47": ">2>2"})
    mocker.patch('builtins.input', side_effect=tested_inputs)

    expected = (expected_menu +
                'rot13: znzn\n'
                'rot47: >2>2\n' +
                expected_menu +
                "Goodbye!\n")

    menu_mock.show_menu()

    captured = capsys.readouterr()
    assert captured.out == expected


def test_show_menu_and_input_5(mocker, capsys, get_menu_mock):
    menu_mock = get_menu_mock
    mocker.patch('builtins.input', return_value='5')
    menu_mock.show_menu()
    expected = (expected_menu +
                'Goodbye!\n')
    captured = capsys.readouterr()
    assert captured.out == expected
