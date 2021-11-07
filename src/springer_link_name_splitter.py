'''
The CSV export of Springer Link exports the names of the authors in a weird format.
Example: First AuthorSecond AuthorThird Author
Therefore we copy the full column and save it to a .txt file.
Then run this script and copy the output from the console to excel.
Then we have our authors in reasonable arrangement
'''

with open('test.txt', encoding='utf') as f:
    for line in f:
        current_authors = line.strip()
        new_string = ""
        for i, v in enumerate(current_authors):
            if i != 0:
                if current_authors[i].isupper():
                    if current_authors[i-1] != " " and current_authors[i-1] != "-":
                        new_string = new_string+"; "
            new_string = new_string + current_authors[i]

        print(new_string)


