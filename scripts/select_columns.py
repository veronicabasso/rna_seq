# This file reads a text file, and produces another text file which contains the selected columns
# from the original text file.

import csv

name = input("Please provide the differentially expressed genes file without file extensions (no .txt)? ")
filename = "./" + name + ".txt"

n_cols = input("Please provide the number of columns, you want to extract: ")
cols = []
for i in range(int(n_cols)):
    col_name = input("cloumn {}: ".format(i + 1))
    cols.append(col_name)

print("You provided the following colums:")
for col in cols:
    print (col)

try:
    inp_file = open(filename, "r")
    print("{} file read successfully".format(filename))
    lines = inp_file.readlines()
    print("First row: ")
    print(lines[0])
    col_ids = []
    for col in cols:
        found = False
        for i, fr_col in enumerate(lines[0]):
            if col == fr_col:
                found = True
                col_ids.append(i)
                col_ids.append(i + 1)
                col_ids.append(i + 2)
                break
        if found == False:
            print("Couldn't find column: {}".format(col))

    '''
    for col_id in col_ids:
        print(lines[0][col_id])

    result = []
    for line in lines:
        result.append(line.split('\t')[0])
    # print(result)
    inp_file.close()
    # print(inp_file.read())
    '''
except (OSError, IOError) as e:
    print("I/O error({0}): {1}".format(e.errno, e.strerror))

'''
out_file = input("Please provide the output filename without file extensions (no .txt)? ")
out_file += ".txt"

with open(out_file, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in result:
        writer.writerow([val])
'''
