# SEC.400_EDA_group
AccountAccessSet custom scripts and datasets. Some .ipynb analysis too.

Research questions:

RQ1. What types of stolen information are traded?
RQ2. What are the prices for different product types?

From: https://zenodo.org/record/8047205

The script product_description.py is a customized version of example_prices.py script from the original AccountAccessSet.zip file downloaded from zenodo.org. To run the customized script you need the JSON-database from the original zip-file. 

You can create your own keyword list in keywords.txt file. Run the label_by_keyword.py script in the same folder with products.csv (generated using product_descriptions.py). Now you have the product labels in a new column.

WordCounter counts how frequently words and word combinations appear in products.csv description-column. Result can be found in words_count.csv.

## Data analysis

The PriceAnalysis.ipynb file is used for analyzing the labeled dataset grouped by keywords (category-column). The keywords are loaded from a txt-file. Please note that the Plotly-graphs can not be rendered by Github code preview. Open the .ipynb file locally or use https://nbviewer.org/github/Niittyv/SEC.400_EDA_group/blob/Additional-features-and-analysis/PriceAnalysis.ipynb
