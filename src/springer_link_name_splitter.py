'''
The CSV export of Springer Link exports the names of the authors in a weird format.
Example: First AuthorSecond AuthorThird Author
Therefore we copy the full column and save it to a .txt file.
Then run this script and copy the output from the console to excel.
Then we have our authors in reasonable arrangement
'''
from tkinter import filedialog as fd
import pandas as pd
from utils import config

column_name = 'Authors'


def everything_is_capitalized(check_string: str) -> bool:
    chars_are_cap = True
    if any(char for char in check_string if char.islower()):
        chars_are_cap = False
    return chars_are_cap


filename = fd.askopenfile()
df = pd.read_csv(filename.name)
author_column = df[column_name]

updated_authors = []

for column in author_column:
    author_string = ''
    print_string = ''

    if pd.notna(column):
        print_string = column
        if not everything_is_capitalized(column):
            for char_index, current_char in enumerate(column):
                if char_index != 0:
                    if current_char.isupper():
                        if column[char_index - 1] != " " and column[char_index - 1] != "-":
                            author_string = author_string + "; "
                author_string = author_string + current_char
            print_string = author_string
    updated_authors.append(print_string)

df_2 = pd.DataFrame(updated_authors, columns=['Updated Authors'])

result = pd.concat([df, df_2], axis=1, join='inner')

result.to_csv("output_df.csv", index=False, encoding=config.text_encoding)
