import pandas as pd

# Load your dataset
df = pd.read_csv("olist_order_items_dataset.csv")
df_products = pd.read_csv("olist_products_dataset.csv")

# Merge product names
df = df.merge(df_products[['product_id', 'product_category_name']], on='product_id', how='left')

# Create category set per order
df_grouped = df.groupby('order_id')['product_category_name'].apply(
    lambda x: ','.join(sorted(set(x)))
).reset_index(name='category_set')

# Count frequency of each combination
category_counts = df_grouped['category_set'].value_counts().reset_index()
category_counts.columns = ['category_set', 'order_count']

category_counts.to_csv("category_sets.csv", index=False)
