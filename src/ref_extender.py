''''
This is used to extend the reference csv with the associated references, as a preliminary work for the duplicate finder
'''

from tkinter import filedialog as fd

import csv

filename = fd.askopenfile()

filename = filename.name
directory = filename.rsplit('/', 1)[0]
prefix = filename.split('/')[-1].split('.')[0]

output_file = open(directory + '/' + prefix + '_extended.csv', 'w', encoding="utf-8")
output_file.truncate(0)


with open(filename, newline='', encoding='utf-8') as csvfile:
    data = list(csv.reader(csvfile))

csv_row = f"ref;title\n"
output_file.write(csv_row)

for date in data:
    csv_row = f"{prefix};{date[0]}\n"
    output_file.write(csv_row)

output_file.close()
