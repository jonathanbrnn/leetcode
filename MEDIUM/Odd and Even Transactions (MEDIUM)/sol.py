import pandas as pd

def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    dic = defaultdict(lambda: [0, 0])
    dates = []
    transactions.sort_values(by="transaction_date", ascending=True, inplace=True)

    for amount, date in zip(transactions["amount"], transactions["transaction_date"]):
        if date not in dates:
            dates.append(date)

        if amount % 2 == 0:
            dic[date][1] += amount
        else:
            dic[date][0] += amount

    odd = []
    even = []

    for date in dates:
        odd.append(dic[date][0])
        even.append(dic[date][1])

    return pd.DataFrame({"transaction_date": dates, "odd_sum": odd, "even_sum": even})
