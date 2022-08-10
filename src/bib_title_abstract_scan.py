'''
This can be used to export from bib files.
For example from ACM or IEEE!
'''
from typing import List, Set

from pybtex.database.input import bibtex
from utils import utils, config

from tkinter import filedialog as fd

import re

data_folder, files = utils.get_files_with_type_from_folder('.bib')

output_file = open(data_folder + '/output.txt', 'w', encoding=config.text_encoding)
join_string = config.join_string


def get_entries_with_abstract_scan(files: List, headlines: Set) -> List:
    # Second, when we have all possible headlines from all files, we can use these to fill the output

    # open a bibtex file
    parser = bibtex.Parser()
    outputs = []

    bpmn_pattern = r"(bpmn|business process model and notation|business process model*)"
    secure_pattern = r"secur*"
    extension_pattern = r"exten*|annota*"

    for file_to_open in files:
        outputs = []
        bibdata = parser.parse_file(file_to_open)

        for bib_id in bibdata.entries:
            current_entry = bibdata.entries[bib_id]

            paper_abstract = str(current_entry.fields.get('abstract'))
            paper_title = str(current_entry.fields.get('title'))

            if (re.search(bpmn_pattern, paper_abstract, re.IGNORECASE)
                    and re.search(secure_pattern, paper_abstract, re.IGNORECASE)
                    and re.search(extension_pattern, paper_abstract, re.IGNORECASE))\
                    or\
                    (re.search(bpmn_pattern, paper_title, re.IGNORECASE)
                     and re.search(secure_pattern, paper_title, re.IGNORECASE)
                     and re.search(extension_pattern, paper_title, re.IGNORECASE)):

                current_entry_string = utils.get_entry_as_string(current_entry, headlines, join_string)
                outputs.append(current_entry_string)

    return outputs


titles = utils.get_headlines(files)
entries = get_entries_with_abstract_scan(files, titles)


title_row = f'{join_string.join(titles)}{join_string}Authors\n'
output_file.write(title_row)
for entry in entries:
    print(entry)
    output_file.write(entry)
output_file.close()
