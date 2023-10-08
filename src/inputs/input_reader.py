import re

class InputReader:
    @staticmethod
    def get_user_input(message_to_user):
        while True:
            user_input = input(message_to_user)
            if not InputReader.contains_polish_characters(user_input):
                return user_input
            print("Don't use polish characters")

    @staticmethod
    def contains_polish_characters(check_this_text):
        pattern = re.search("[ąĄćĆęĘłŁńŃóÓśŚżŻźŹ]", check_this_text)
        return pattern
