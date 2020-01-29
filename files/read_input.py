from files.filehandler import *

user_in = filehandler.get_array()


class ReadInput:

    def __init__(self, raw_text):
        self.__raw_text = [user_in]

    def text_to_array(self):
        return self.__raw_text


read_input = ReadInput(user_in)
