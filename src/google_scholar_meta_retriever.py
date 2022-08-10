from utils import utils, config

from bs4 import BeautifulSoup

data_folder, files = utils.get_files_with_type_from_folder('.html')

output_file = open(data_folder + '/output.txt', 'w', encoding=config.text_encoding)

for file_to_open in files:
    with open(file_to_open, encoding=config.text_encoding) as fp:
        soup = BeautifulSoup(fp, 'html.parser')

        articles = soup.find_all("div", class_="gs_r gs_or gs_scl")
        for article in articles:
            title_element = article.find("h3", class_="gs_rt")
            try:
                title = title_element.find('a').get_text()
            except AttributeError:
                spans = title_element.find_all("span")
                span = spans[-1]
                title = span.get_text()

            author_element = article.find("div", class_="gs_a")
            # not possible via finding 'a' in element, because only authors with link are 'a',
            # without link they are just plaintext
            authors = author_element.get_text().split('-', 1)[0]

            # write output
            csv_row = f"{title}{config.join_string}{authors}\n"
            output_file.write(csv_row)
            print(csv_row)

output_file.close()

