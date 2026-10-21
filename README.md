# SEC.400_EDA_group
AccountAccessSet custom scripts and datasets. Some .ipynb analysis too.

Research questions:

RQ1. What types of stolen information are traded?
RQ2. What are the prices for different product types?

From: https://zenodo.org/record/8047205

The script product_description.py is a customized version of example_prices.py script from the original zip-file downloaded from zenodo.org. To run the customized script you need the JSON-database from the original zip-file. 

You can create your own keyword list in keywords.txt file. Run the label_by_keyword.py script in the same folder with products.csv (generated using product_description.py). Now you have the product labels in a new column.

WordCounter counts how frequently words and word combinations appear in products.csv description-column. Result can be found in words_count.csv.
