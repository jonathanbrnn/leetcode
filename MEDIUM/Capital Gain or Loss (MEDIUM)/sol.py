import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    stocks.sort_values(by="operation_day")
    dic = defaultdict(list)
    capital_gain_loss = defaultdict(int)

    for stock, price, operation in zip(stocks["stock_name"], stocks["price"], stocks["operation"]):
        if str(operation) == "Buy":
            dic[stock].append(price)
        else:
            buy_price = dic[stock].pop(0)
            capital_gain_loss[stock] += price - buy_price

    name = []
    gain_loss = []

    for item, val in capital_gain_loss.items():
        name.append(item)
        gain_loss.append(val)

    return pd.DataFrame({"stock_name": name, "capital_gain_loss": gain_loss})
