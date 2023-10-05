import re

class InputReader:
    @staticmethod
    def get_user_input(message_to_user):
        while True:
            user_input = input(message_to_user)
            if InputReader.text_validation(user_input):
                return user_input
            else:
                print("Don't use Polish signs")

    @staticmethod
    def text_validation(check_this_text):
        pattern = re.match("[^ąĄćĆęĘłŁńŃóÓśŚżŻźŹ]+$", check_this_text)
        return pattern
