import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    immediate = 0
    total_first = 0
    seen = set()

    delivery.sort_values(by="order_date", inplace=True)

    for customer_id, order_date, pref in zip(delivery["customer_id"], delivery["order_date"], delivery["customer_pref_delivery_date"]):
        if order_date == pref and customer_id not in seen:
            immediate += 1
            total_first += 1
        elif customer_id not in seen:
            total_first += 1

        seen.add(customer_id)

    immediate_percentage = round((immediate / total_first) * 100, 2) if total_first > 0 else 0
    return pd.DataFrame({"immediate_percentage": [immediate_percentage]})
