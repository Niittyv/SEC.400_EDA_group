import pandas as pd
import re

#edit the keywords to your liking
#keywords = ["tax", "online access", "full info"]

with open("keywords.txt", encoding="utf-8") as f:
    keywords = [line.strip() for line in f if line.strip()]

print(keywords)

df = pd.read_csv('products.csv')

def find_keywords(description):
    if pd.isna(description):
        return None
    found = [k for k in keywords
            if re.search(re.escape(k), description, flags=re.IGNORECASE)]
    return ", ".join(found) if found else None

df["category"] = df["description"].apply(find_keywords)

#write results to file
filename = "products_labeled.csv"
df.to_csv(filename, index=False)