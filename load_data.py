import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

DB_USER = "postgres"
DB_PASSWORD = quote_plus("Westhaven@161")
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "business_intelligence"

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

files = {
    "customers": "data/olist_customers_dataset.csv",
    "orders": "data/olist_orders_dataset.csv",
    "order_items": "data/olist_order_items_dataset.csv",
    "order_payments": "data/olist_order_payments_dataset.csv",
    "order_reviews": "data/olist_order_reviews_dataset.csv",
    "products": "data/olist_products_dataset.csv",
    "sellers": "data/olist_sellers_dataset.csv",
    "product_category_translation": "data/product_category_name_translation.csv",
    "geolocation": "data/olist_geolocation_dataset.csv",
}

for table_name, file_path in files.items():
    print(f"Loading {table_name}...")
    df = pd.read_csv(file_path)
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"{table_name}: {len(df)} rows loaded")

print("All Olist datasets loaded successfully.")