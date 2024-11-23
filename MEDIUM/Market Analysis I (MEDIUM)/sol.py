import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    user_orders = defaultdict(int)

    for buyer_id, order_date in zip(orders["buyer_id"], orders["order_date"]):
        if "2018-12-31" < str(order_date)[:10] < "2020-01-01":
            user_orders[buyer_id] += 1

    ids = []
    join_dates = []
    orders_2019 = []

    for user_id, join_date in zip(users["user_id"], users["join_date"]):
        ids.append(user_id)
        join_dates.append(join_date)
        orders_2019.append(user_orders[user_id])

    return pd.DataFrame({"buyer_id": ids, "join_date": join_dates, "orders_in_2019": orders_2019})
