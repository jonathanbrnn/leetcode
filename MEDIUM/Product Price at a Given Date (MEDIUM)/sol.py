import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    products.sort_values(by="change_date", inplace=True)
    dic = defaultdict(int)

    for prod_id, price, date in zip(products["product_id"], products["new_price"], products["change_date"]):
        if str(date) <= "2019-08-16 00:00:00":
            dic[prod_id] = price
        elif prod_id not in dic and str(date) > "2019-08-16 00:00:00":
            dic[prod_id] = 10


    ids = []
    prices = []

    for item, val in dic.items():
        ids.append(item)
        prices.append(val)


    return pd.DataFrame({"product_id": ids, "price": prices})
