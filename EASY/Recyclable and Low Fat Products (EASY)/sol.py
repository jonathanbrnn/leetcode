import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    ids = []

    for prod, fats, recy in zip(products["product_id"], products["low_fats"], products["recyclable"]):
        if fats == "Y" and recy == "Y":
            ids.append(prod)

    return pd.DataFrame({"product_id": ids})
