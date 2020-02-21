from files.read_input import *
from files.crypt_one_base import *

i = 0

# store input content in new string

array_to_crypt_one = str(read_input.text_to_array())
array_crypted = []
len_array = len(array_to_crypt_one)

while i < len_array:
    if array_to_crypt_one[i] in crypt_one_base_dict:
        array_crypted.append(crypt_one_base_dict[array_to_crypt_one[i]])

    i+=1

class Crypt_Step_One:

    def __init__(self):

        pass