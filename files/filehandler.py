import json

# this file is the input file from the user
with open("../input_files/text_file.json", "r", encoding='utf-8') as file:
    data_file = json.load(file)
    text_array = data_file['text_to_code']

class Filehandler:

    def __init__(self, array):
        self.__array = array

#file get stored in an lowercase array
    def get_array(self):
        return self.__array['input'].strip().lower()


filehandler = Filehandler(text_array)