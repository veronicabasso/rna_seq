# This file reads a text file, and produces another text file which contains the selected columns
# from the original text file.
#
# Format the LIBRARIES.txt file:
# :%s/^M/\r/g
# To get a ^M, you need to do Ctrl-V followed by Ctrl-M

import csv
import re

name = input("Please provide the differentially expressed genes file without file extensions (no .txt)? ")
filename = "./" + name + ".txt"

try:
    inp_file = open(filename, "r")
    print("{} file read successfully".format(filename))
    lines = inp_file.readlines()
    print("First row: ")
    print(lines[0])

    n_cols = input("Please provide the number of columns, you want to extract: ")
    cols = []
    for i in range(int(n_cols)):
        col_name = input("cloumn {}: ".format(i + 1))
        cols.append(col_name)

    print("You provided the following colums:")
    for col in cols:
        print (col)

    conditions_all = []
    for col in cols:
        nums = re.findall(r'\d+', col)
        conditions_all.append(nums[0])
        conditions_all.append(nums[1])
    conditions = sorted(set(conditions_all))

    print("We are going to extract the following conditions: ")
    print(conditions)

    try:
        lib_file = open("./LIBRARIES.txt", "r")
        lines_lib = lib_file.readlines()
        libnames = []
        for cond in conditions:
            for line in lines_lib:
                line_cols = line.split('\t')
                if len(line_cols) > 7:
                    if line_cols[5] == cond:
                        libnames.append(line_cols[0])
        print("Library names: ")
        print(libnames)

    except (OSError, IOError) as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))

    fr_cols = lines[0].split('\t')
    col_ids = []
    for col in cols:
        found = False
        for i, fr_col in enumerate(fr_cols):
            # print ("compare: {}, {}".format(col, fr_col))
            if col == fr_col:
                found = True
                col_ids.append(i)
                col_ids.append(i + 1)
                col_ids.append(i + 2)
                break
        if found == False:
            print("Couldn't find column: {}".format(col))

    print ("Going to extract the following columns:")
    for col_id in col_ids:
        print(fr_cols[col_id])

    results = []
    for line in lines:
        fr_cols = line.split('\t')
        row = []
        for col_id in col_ids:
            row.append(fr_cols[col_id])
        results.append(row)

    # print(results)
    inp_file.close()
    # print(inp_file.read())
except (OSError, IOError) as e:
    print("I/O error({0}): {1}".format(e.errno, e.strerror))

out_file = input("Please provide the output filename without file extensions (no .txt)? ")
out_file += ".txt"

with open(out_file, "wb") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerow(results)
