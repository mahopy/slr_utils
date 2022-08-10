import os
from typing import List, Set, Tuple
from tkinter import filedialog as fd

from pybtex.database.input import bibtex


def get_files_with_type_from_folder(file_type: str) -> Tuple[str, List]:
    data_folder = fd.askdirectory()
    files = []
    for file in sorted(os.listdir(data_folder)):
        if file.endswith(file_type):
            files.append(data_folder+'/'+file)

    return data_folder, files


def get_entry_as_string(entry, headlines, join_string) -> str:
    authors = []
    for author in entry.persons["author"]:
        first_name = ""
        last_name = ""
        if len(author.first_names) > 0:
            first_name = author.first_names[0]
        if len(author.last_names) > 0:
            last_name = author.last_names[0]
        authors.append(f'{first_name} {last_name}')
    author_string = ', '.join(authors)

    current_run = []
    for key in headlines:
        current_value = entry.fields.get(key, 'None')
        if current_value == '':
            current_value = 'None'
        current_run.append(current_value)
    return f'{join_string.join(current_run)}{join_string}{author_string}\n'


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
