import fitz
import re

from tkinter import filedialog as fd
from stop_words import get_stop_words
stop_words = get_stop_words('english')

from collections import Counter
scan_words = ['']

import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

from utils import utils as ut

lemmatizer = WordNetLemmatizer()

folder = fd.askdirectory()
files = ut.get_files_with_type_from_folder(folder, '.pdf')

for file in files:

    doc = fitz.open(file)

    complete_content = ""
    for page in doc:
        text = page.get_text('text')
        complete_content += f' {text}'

    splitted_content = complete_content.split()

    is_body = False
    is_reference = False
    body = ""
    references = ""
    filtered_list = []
    for word in splitted_content:
        if word == "INTRODUCTION" or word == "Introduction":
            is_body = True
        if word == "References" or word == "REFERENCES":
            is_body = False
            is_reference = True

        if is_body:
            body += f' {word}'
        if is_reference:
            references += f' {word}'

    body = body.lower()
    body = body.replace('- ', '').replace(',', '').replace('.','')
    body = re.sub('\s?\[.*?\]', '', body).strip()

    # remove stopwords
    split_list = body.split()
    for word in split_list:
        if word not in stop_words:
            filtered_list.append(word)

    # stem words
    stemmed_list = []
    for word in filtered_list:
        stemmed_list.append(lemmatizer.lemmatize(word))

    # count words
    counted_list = Counter(stemmed_list)

    current_file = file.rsplit('/', 1)[1]
    print(f'---- {current_file} ----')
    # print(counted_list.most_common())
    print(f'{references}')
