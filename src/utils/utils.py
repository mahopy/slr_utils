import os
from typing import List


def get_files_with_type_from_folder(folder: str, file_type: str) -> List:
    files = []
    for file in sorted(os.listdir(folder)):
        if file.endswith(file_type):
            files.append(folder+'/'+file)

    return files


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
