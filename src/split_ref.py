from tkinter import filedialog as fd

import csv

filename = fd.askopenfile()
filename = filename.name
prefix = filename.split('/')[-1].split('.')[0]

directory = filename.rsplit('/', 1)[0]
output_file = open(directory + '/' + prefix + '_splitted.csv', 'w', encoding="utf-8")
output_file.truncate(0)

with open(filename, newline='', encoding='utf-8') as csvfile:
    data = list(csv.reader(csvfile))

for ref in data:
    string = ''.join(ref)
    first = string.split(".:", 1)

    try:
        second = first[1].split(".", 1)
    except IndexError:
        second = first[0].split(".", 1)

    output_string = ""
    for data in second:
        output_string = first[0] + ";" + second[0]

    print(output_string)

