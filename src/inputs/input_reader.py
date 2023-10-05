import re


class InputReader:
    @staticmethod
    def get_user_input(message_to_user):
        user_input = input(message_to_user)
        if InputReader.text_validation(user_input):
            return user_input
        else:
            print("Don't use polish signs")

    @staticmethod
    def text_validation(check_this_text):
        pattern = re.match("^[A-Za-z0-9]+$", check_this_text)
        return pattern
