import fitz

from utils import utils as ut

folder, files = ut.get_files_with_type_from_folder('.pdf')

for file in files:
    article = fitz.open(file)

    complete_content = ""
    for page in article:
        text = page.get_text('text')
        complete_content += f' {text}'

    splitted_content = complete_content.split()

    is_reference = False
    references = ""

    for word in splitted_content:
        if is_reference:
            references += f' {word}'

        if word == "References" or word == "REFERENCES":
            is_reference = True



    current_file = file.rsplit('/', 1)[1]
    print(f'---- {current_file} ----')
    print(f'{references}')
