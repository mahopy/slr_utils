import json

import crossref_commons.retrieval as ccr
import requests

import csv

import sqlite3

con = sqlite3.connect('example.db')


def row_exists(table_name: str, attribute: str, search_str: str) -> bool:
    row_cursor = con.cursor()
    row_cursor.execute(f"SELECT rowid FROM {table_name} where {attribute}=?", (
    search_str,))
    data = row_cursor.fetchall()
    return_type = False
    if len(data) > 0:
        return_type = True
    return return_type


def create_table(table_name: str):
    create_cursor = con.cursor()
    # Create table
    create_cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} "
                          f"(id text,"
                          f" title text, doi text, duplicate boolean not null default 0, original text, ref text)")
    con.commit()


def insert_values(table_name: str, values: str):
    insert_cursor = con.cursor()
    insert_cursor.execute(f"INSERT INTO {table_name} VALUES ({values})")
    con.commit()

def get_rows(table_name: str):
    get_cursor = con.cursor()
    get_cursor.execute(f"Select * from {table_name}")
    rows = get_cursor.fetchall()
    con.commit()

    return rows


def get_value(table_name: str, goal_attributes: str, search_str: str):
    get_cursor = con.cursor()
    get_cursor.execute(f'Select {goal_attributes} from {table_name} WHERE {search_str}')
    attributes = get_cursor.fetchall()
    con.commit()
    return attributes

def sql_work():
    title = "Data-Driven Workflow Management by Utilising BPMN and CPN in IIoT Systems with the Arrowhead Framework"
    if row_exists('acm_is', 'title', title):
        print('somethong')
    else:
        values = ('acm_is_1', title,'10.1109/ETFA.2019.8869501',0, 'None', 'None')
        insert_values('acm_is', values)

    rows = get_rows('acm_is')

    for row in rows:
        print(row)

    my_value = get_value('acm_is', 'doi', 'title = "Advances in Business ICT: New Ideas from Ongoing Research"')
    print(my_value)


sql_work()
# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()

#
# from tkinter import filedialog as fd
# from bs4 import BeautifulSoup
#
# filename = fd.askopenfile()
#
# filename = filename.name
# directory = filename.rsplit('/', 1)[0]
# prefix = filename.split('/')[-1].split('.')[0]
#
# research_title = "Framework of Integrated System for the Innovation of Mold Manufacturing through Process Integration and Collaboration"
# # research_title = "Lorem Ipsum None est"
#
#
# with open(filename, newline='', encoding='utf-8') as csvfile:
#     data = list(csv.reader(csvfile))
#
# for i in range(1, len(data)):
#     my_list = data[i][0].split(';')
#
#     doi = my_list[2]
#     if doi is None:
#     # response = requests.get(f"https://dblp.org/search/publ/api?q={research_title}")
#     #
#     # xmldoc = response.text
#     #
#     # doc = BeautifulSoup(xmldoc, 'lxml')
#     # try:
#     #     ieee_code = doc.find('doi').get_text()
#     #     ext_doc = ccr.get_publication_as_json(ieee_code)
#     #
#     #     references = ext_doc.get('reference')
#     #
#     #     ref_string = None
#     #     if references is not None:
#     #         ref_string = references
#     #     print(ref_string)
#     #
#     # except AttributeError:
#     #     print('Document not found')
