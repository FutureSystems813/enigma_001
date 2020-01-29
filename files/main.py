from files.read_input import *

file_content = read_input.text_to_array()

def generate_csv():
    with open("C:/enigma/codec_file.csv", "w+") as coded_file:
        for line in file_content:
            coded_file.write(line)

generate_csv()


# import os
# path = "C:/enigma"
# try:
#   os.mkdir(path)
# except OSError:
#   print("creation failed %s " % path)
# else
#   print("succes %s " % path)