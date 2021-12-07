from typing import List

term_collection = [['bpmn', '"business process management and notation"'],
               ['IIoT', '"Industrial Internet of Things"', '"Cyber Physical Systems"', 'CPS', 'CPPS', '"Industrial Control Systems"', 'ICS', '"Supervisory Control and Data Acquisition"', 'SCADA', '"Industrial Internet"', '"Industry 4.0"', 'manufacturing']]


def make_packages(terms, term_collection, prefix=''):
    search_query = ''
    if prefix != '':
        prefix = f'{prefix}:'
    for term in terms:
        separator = ''
        if terms.index(term) != 0:
            separator = ' OR '
        search_query += separator + prefix + term
    search_query += ')'
    if term_collection.index(terms) != len(term_collection) - 1:
        search_query += ' AND '
    return search_query


def get_ieee_string(prefix_list: List, term_collection) -> str:
    search_query = '('
    for prefix in prefix_list:
        search_query += '('
        for terms in term_collection:
            search_query += '('
            search_query += make_packages(terms, term_collection, prefix)
        if prefix_list.index(prefix) != len(prefix_list)-1:
            search_query += ') OR '
        else:
            search_query += ')'

    search_query += ')'
    return search_query


def get_springer_string(term_collection):
    output_string = ''
    for terms in term_collection:
        output_string += '('
        output_string += make_packages(terms, term_collection)
    return output_string
    

def get_acm_string(prefix, term_collection):
    output_string = ''
    for terms in term_collection:
        output_string += f'{prefix}:('
        output_string += make_packages(terms, term_collection)
    return output_string


ieee_prefix = ['"Title"', '"Abstract"']
ieee_string = get_ieee_string(ieee_prefix, term_collection)

acm_prefix = 'Title'
acm_string = get_acm_string(acm_prefix, term_collection)
sp_string = get_springer_string(term_collection)

print(f'Ieee\nLink: https://ieeexplore.ieee.org/search/searchresult.jsp?action=search&matchBoolean=true&newsearch=true&queryText={ieee_string} \nString: {ieee_string}')
print(f'ACM\nString: {acm_string}')
print(f'Springer: {sp_string}')
print(f'SD: Title, abstract, keywords:{sp_string}')