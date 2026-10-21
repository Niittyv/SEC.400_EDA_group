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

def prices_from_text(text_str):
    ''' All USD prices from the text_str to a sorted integer list '''
    number_list = []
    text_str = text_str.replace('Tutorials and Guides', '').replace('Wallets Botnet logs', '')
    text_lower = text_str.lower()
    if 'guide' in text_lower or 'botnet' in text_lower:
        return number_list
    if not '$**' in text_str:
        return number_list
    # Search prices
    regex = r'\s\*\*\d+\$\*\*\s'
    for line in text_str.split('\n'):
        line = line.lower()
        if not '**' in line or not '$' in line:
            continue
        if 'mix' in line: # Skip mixed data packages
            continue
        # Skip 0 pcs or more than 1 pcs
        skip_this = False
        for pcs in ['0', '2', '3', '4', '5', '6', '7', '8', '9']:
            for word in ['pcs', 'piece']:
                if pcs + word in line or pcs + ' ' + word in line:
                    skip_this = True
                    break
        if skip_this:
            continue
        for number in re.findall(regex, line):
            number = float(number.replace('*', '').replace('$', '').strip())
            if 0 < number < 1000000: # More than zero and less than million
                #print('Example line %d: %s' % (len(number_list) + 1, line.strip()))
                number_list.append(number)
    number_list.sort()
    return number_list


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

def get_price_statistics(text_str, title):
    ''' Get price aggregates: mean, median, max, min, count '''
    zero_output = [0,0,0,0,0]
    if 'guide' in title.lower() or 'tutorial' in title.lower():
        return zero_output
    if 'package' in title.lower() or 'bulk' in title.lower():
        return zero_output
    price_list = prices_from_text(text_str)
    if len(price_list) < 1:
        return zero_output
    mean_price = pd.Series(price_list).mean()
    median_price = pd.Series(price_list).median()
    max_price = max(price_list)
    min_price = min(price_list)
    count_price = len(price_list)
    return [mean_price, median_price, max_price, min_price, count_price]



def products_information(inputfile):
    ''' Get the title and description from inputfile '''
    assert os.path.isfile(inputfile)
    item = read_json(inputfile)
    assert item
    text = item.get('text', '')
    assert len(text) > 100

    title = get_title_from_text(text)
    description = get_description_from_text(text)

    aggregates = get_price_statistics(text, title)

    #print(title)
    #print("\n")
    #print(description)
    #print("\n")
    #print(aggregates)
    #print("\n")

    output = [inputfile, title, description]
    output.extend(aggregates)

    #print(output)
    #print("\n")

    return output


product_pages_used = 0

df_format = {
    "inputfile" : [],
    "product" : [],
    "description" : [],
    "mean_price" : [],
    "median_price" : [],
    "max_price" : [],
    "min_price" : [],
    "prices_count" : []
}

dataframe = pd.DataFrame(data=df_format)

for key, value_list in FILE_LIST.items():
    print(key.replace('_', ' ').upper())
    for value in value_list:
        #print("opened {}".format(value))
        if str(value) in SKIP_LIST:
            continue
        if 'database' in str(value):
            #print("opened {}".format(value))
            new_product = products_information(value)
            #print(new_product)
            #print("\n")       
            if new_product:
                #print(new_product)
                #print("\n")       
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
dataframe.to_csv(filename)




