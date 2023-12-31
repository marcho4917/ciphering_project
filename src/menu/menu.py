from src.ciphering.rot13 import Rot13
from src.ciphering.rot47 import Rot47
from src.files.file_handler import FileHandler
from src.inputs.input_reader import InputReader


class Menu:
    def __init__(self):
        self.input_reader = InputReader()
        self.rot13 = Rot13()
        self.rot47 = Rot47()
        self.file_handler = FileHandler()
        self.text_dict = {}
        self.encrypted_text = None

    def show_menu(self):
        while True:
            print("1. Encrypt plain text (ROT47/ ROT13)")
            print("2. Save encrypted text to file")
            print("3. Decrypt encrypted text from file")
            print("4. Print encrypted words stored in memory")
            print("5. Exit")

            option = self.input_reader.get_user_input("Chose option: ")

            if option == "1":
                text_to_encrypt = self.input_reader.get_user_input("Write your text: ")
                rot_type =self.input_reader.get_user_input("ROT13 or ROT47: ").lower()
                if rot_type in ('rot13', 'rot47'):
                    self.encrypted_text = getattr(self, rot_type).encrypt(text_to_encrypt)
                # if rot_type.lower() == "rot13":
                #     self.rot13.encrypt(text_to_encrypt)
                # elif rot_type.lower() == "rot47":
                #     self.rot47.encrypt(text_to_encrypt)
                else:
                    print("Wrong rot type!")
                self.text_dict.update({rot_type: self.encrypted_text})
            elif option == "2":
                if self.encrypted_text is not None:
                    filename = self.input_reader.get_user_input("Give filename: ")
                    self.file_handler.save_to_file(filename, self.text_dict)
                else:
                    print("You have to encrypt text first!")
            elif option == "3":
                filename = self.input_reader.get_user_input("Chose file with text to decrypt: ")
                for rot_type, encrypted_text in self.file_handler.read_from_file(filename).items():
                    decrypted_text = getattr(self, rot_type).decrypt(encrypted_text)
                    print(f"Your text after decrypt it is: {decrypted_text}")
            elif option == "4":
                for k, v in self.text_dict.items():
                    print(f"{k}: {v}")
            elif option == "5":
                print("Goodbye!")
                break


