# SEC.400_EDA_group

AccountAccessSet custom scripts and datasets. Some .ipynb analysis too.

Research questions:

RQ1. "What keywords and subcategories exist within personal information products sold on the dark web marketplaces?" 

RQ2. "What is the total market share of personal information products?"

RQ3. "What are the price distributions for personal information products?"

From: https://zenodo.org/record/8047205

The script product_description.py is a customized version of example_prices.py script from the original AccountAccessSet.zip file downloaded from zenodo.org. To run the customized script you need the JSON-database from the original zip-file. 

You can create your own keyword list in keywords.txt file. Run the label_by_keyword.py script in the same folder with products.csv (generated using product_descriptions.py). Inside label_by_keyword.py there is a dictionary of keyword synonyms that exists to bundle synonym keywords into one category. Now you have the product labels in a new 'category'-column.

WordCounter counts how frequently words and word combinations appear in products.csv description-column. Result can be found in words_count.csv.

## Data analysis

The PriceAnalysis.ipynb file is used for analyzing the labeled dataset grouped by keywords (category-column). The keywords are loaded from a notebook_keyword.txt file. 

Please note that the Plotly-graphs can not be rendered by Github code preview. Open the .ipynb file locally or use https://nbviewer.org/github/Niittyv/SEC.400_EDA_group/blob/Product-category-analysis/PriceAnalysis.ipynb

Please remember to remove synonym keywords bundled together earlier in label_by_keyword.py script from notebook_keywords.txt file!

## Project flow

<img width="761" height="152" alt="AnalysisFlow" src="https://github.com/user-attachments/assets/46486c45-f72e-4d08-a60a-31f10a9c4c68" />

