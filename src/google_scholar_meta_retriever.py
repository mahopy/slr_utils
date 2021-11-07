from utils import utils

from tkinter import filedialog as fd
from bs4 import BeautifulSoup

data_folder = fd.askdirectory()
files = utils.get_files_with_type_from_folder(str(data_folder), '.html')

output_file = open(data_folder + '/output.txt', 'w', encoding="UTF-8")
output_file.truncate(0)

for file_to_open in files:
    with open(file_to_open, encoding='utf8') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        elements = soup.find_all("h3", class_="gs_rt")
        for element in elements:
            try:
                title = element.find('a').get_text()
            except AttributeError:
                spans = element.find_all("span")
                span = spans[-1]
                title = span.get_text()

            # write output
            csv_row = f"{title}\n"
            output_file.write(csv_row)
            print(title)

output_file.close()

