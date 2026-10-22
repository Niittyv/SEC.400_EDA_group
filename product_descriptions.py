''' Collect data from selected JSON files '''
import os
import re
import json
from glob import glob
import pandas as pd

# These items are datadump collections, skip them
SKIP_LIST = [
    'database/1354.json',
    'database/984.json',
    'database/768.json',
    'database/977.json',
    'database/617.json',
    'database/977.json',
    'database/617.json',
    'database/977.json',
    'database/1286.json',
    'database/1543.json',
    'database/482.json'
]


# Reads all JSON files
FILE_LIST = {
    'Test': glob('database/*.json')
}

def read_json(filename):
    ''' Read JSON file '''
    json_data = {}
    with open(filename, 'r', encoding='utf-8') as myfile:
        json_data = json.load(myfile)
    return json_data

def get_title_from_text(text_str):
    ''' Get the title text '''
    marker = '######'
    first = text_str.find(marker)
    if first == -1:
        return ''

    start = text_str.find(marker, first + len(marker))

    start += len(marker)
    end = text_str.find('#####', start)
    if end == -1:
        end = len(text_str)

    return text_str[start:end].strip()


def get_description_from_text(text_str):
    ''' Get the description text '''
    marker = 'About Product'
    start = text_str.find(marker)
    if start == -1:
        return ''

    start += len(marker)
    end = text_str.find('#####', start)
    if end == -1:
        end = len(text_str)

    return text_str[start:end].strip()

def products_information(inputfile):
    ''' Get the title and description from inputfile '''
    assert os.path.isfile(inputfile)
    item = read_json(inputfile)
    assert item
    text = item.get('text', '')
    assert len(text) > 100
    title = get_title_from_text(text)
    description = get_description_from_text(text)
    return [title, description, inputfile]


product_pages_used = 0

df_format = {
        "product" : [],
        "description" : [],
        "inputfile" : []
}

dataframe = pd.DataFrame(data=df_format)

for key, value_list in FILE_LIST.items():
    print(key.replace('_', ' ').upper())
    for value in value_list:
        if str(value) in SKIP_LIST:
            continue
        if 'database' in str(value):
            new_product = products_information(value)
            if new_product:
                dataframe.loc[len(dataframe)] = new_product
                product_pages_used = product_pages_used + 1
        else:
            new_product = products_information('database/%d.json' % value)
            if new_product:
                dataframe.loc[len(dataframe)] = new_product
                product_pages_used = product_pages_used + 1


print('\nUsed %d product pages' % product_pages_used)

#write results to file
filename = "products.csv"
dataframe.to_csv(filename, index=False)




