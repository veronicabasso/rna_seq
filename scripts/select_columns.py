# This file reads a text file, and produces another text file which contains the selected columns
# from the original text file.

name = input("Please provide the input file without file extensions (no .txt)? ")
filename = "./" + name + ".txt"

try:
    inp_file = open(filename, "r")
    print(inp_file.read)
except (OSError, IOError) as e:
    print("I/O error({0}): {1}".format(e.errno, e.strerror))
