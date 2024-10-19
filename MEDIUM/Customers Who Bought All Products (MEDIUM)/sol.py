import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    res = []
    product_count = len(product["product_key"])
    dic = defaultdict(set)
    skip = set()

    for customer, product in zip(customer["customer_id"], customer["product_key"]):
        if customer not in skip:
            dic[customer].add(product)
            if len(dic[customer]) == product_count:
                res.append(customer)
                skip.add(customer)

    return pd.DataFrame({"customer_id": res})
