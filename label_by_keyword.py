import pandas as pd
import re

# Library of synonym keywords, please add entries as you see fit.
keyword_variants_dict = {
    "credit card": ["cc", "credit_card", "credit-card"],
    "address": ["adress"]
}

with open("keywords.txt", encoding="utf-8") as f:
    keywords = [line.strip() for line in f if line.strip()]

keywords = list(dict.fromkeys(keywords)) #removes duplicates

print(keywords)

df = pd.read_csv('products.csv')

def find_keywords(description):
    if pd.isna(description):
        return None
    description = " ".join(description.split())
    found = [k for k in keywords
            if re.search(re.escape(k), description, flags=re.IGNORECASE)]
    return ", ".join(found) if found else None

df["category"] = df["description"].apply(find_keywords)

# Bundle synonym keywords into one category
for keyword in keyword_variants_dict:
    pattern = r"\b(?:" + "|".join(map(re.escape, keyword_variants_dict[keyword])) + r")\b"
    df["category"] = df["category"].str.replace(pattern, keyword, regex=True, case=False)

#write results to file
filename = "products_labeled.csv"
df.to_csv(filename, index=False)