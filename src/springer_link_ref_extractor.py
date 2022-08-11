from utils import utils

from tkinter import filedialog as fd
from bs4 import BeautifulSoup

data_folder = fd.askdirectory()
files = utils.get_files_with_type_from_folder(str(data_folder), '.html')

output_file = open(data_folder + '/output.txt', 'w', encoding="UTF-8")
output_file.truncate(0)

for file_to_open in files:
    with open(file_to_open, encoding='UTF-8') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        elements = soup.find_all("li", class_="Citation")

        for element in elements:
            try:
                ref_str = element.find("div", class_="CitationContent").get_text()
            except:
                ref_str = 'None'
            # write output
            try:
                authors = ref_str.split(".: ", 1)[0]
            except:
                authors = "None"

            try:
                ref_str = ref_str.split(".: ", 1)[1]
            except:
                ref_str = ref_str


            try:
                title = ref_str.split(". In:", 1)[0]
            except:
                title = "None"

            try:
                ref_str = ref_str.split(". In:", 1)[1]
            except:
                ref_str = ref_str


            # csv_row = f"{title}\n"
            # output_file.write(csv_row)
            print(f"{authors}µ{title}")

output_file.close()