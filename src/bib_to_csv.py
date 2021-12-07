'''
This can be used to export from bib files.
For example from ACM or IEEE!
'''
from typing import List, Set

from pybtex.database.input import bibtex
from tkinter import filedialog as fd

from utils import utils

data_folder = fd.askdirectory()
files = utils.get_files_with_type_from_folder(data_folder, '.bib')

output_file = open(data_folder + '/output.txt', 'w', encoding="UTF-8")
output_file.truncate(0)
join_string = "µ"


def get_headlines(files: List) -> Set:
    # open a bibtex file
    parser = bibtex.Parser()

    headlines = set()
    for file_to_open in files:
        bibdata = parser.parse_file(file_to_open)
        for bib_id in bibdata.entries:
            keys = bibdata.entries[bib_id].fields
            for key in keys:
                headlines.add(key)
    return headlines


def get_entries(files: List, headlines: Set) -> List:
    # Second, when we have all possible headlines from all files, we can use these to fill the output

    # open a bibtex file
    parser = bibtex.Parser()
    outputs = []
    for file_to_open in files:
        outputs = []
        bibdata = parser.parse_file(file_to_open)

        for bib_id in bibdata.entries:
            current_entry = bibdata.entries[bib_id]

            current_entry_string = utils.get_entry_as_string(current_entry, headlines, join_string)
            outputs.append(current_entry_string)

    return outputs


titles = get_headlines(files)
entries = get_entries(files, titles)


title_row = f'{join_string.join(titles)}{join_string}Authors\n'
output_file.write(title_row)
for entry in entries:
    output_file.write(entry)
output_file.close()
