import json


class FileHandler:
    def save_to_file(self, filename, text_dict):
        json_text_dict = json.dumps(text_dict)
        with open(filename, "w") as file:
            file.write(json_text_dict)

    def read_from_file(self, filename):
        with open(filename, "r") as file:
            return file.read()
