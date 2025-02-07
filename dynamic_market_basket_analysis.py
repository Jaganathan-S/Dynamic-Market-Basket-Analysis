pip install pandas mlxtend

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

data = pd.read_excel('sales_data.xlsx')

data['Items'] = data['Items'].str.split(', ')
data = data.explode('Items')


basket = data.groupby(['TransactionID', 'Items']).size().unstack(fill_value=0)

basket = basket.applymap(lambda x: 1 if x > 0 else 0)

frequent_itemsets = apriori(basket, min_support=0.2, use_colnames=True)

rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

print("Frequent Itemsets:")
print(frequent_itemsets)
print("\nAssociation Rules:")
print(rules)

frequent_itemsets.to_excel('frequent_itemsets.xlsx', index=False)
rules.to_excel('association_rules.xlsx', index=False)
