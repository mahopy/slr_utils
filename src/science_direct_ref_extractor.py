from utils import utils

from tkinter import filedialog as fd
from bs4 import BeautifulSoup

data_folder = fd.askdirectory()
files = utils.get_files_with_type_from_folder(str(data_folder), '.html')

output_file = open(data_folder + '/output.txt', 'w', encoding="UTF-8")
output_file.truncate(0)

join_string = "µ"

for file_to_open in files:
    with open(file_to_open, encoding='UTF-8') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        elements = soup.find_all("dd", class_="reference")
        # elements = soup.find_all("strong", class_="title")
        for element in elements:
            # contributor = element.find("div", class_="contribution").get_text()
            try:
                title = element.find("strong", class_="title").get_text()
            except:
                title='None'
            # write output
            csv_row = f"{join_string}{title}\n"
            output_file.write(csv_row)
            print(f"{title}")

output_file.close()

