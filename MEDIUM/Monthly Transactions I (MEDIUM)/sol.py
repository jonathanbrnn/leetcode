def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    dic = defaultdict(lambda: [0, 0, 0, 0])

    for country, state, amount, trans_date in zip(transactions["country"], transactions["state"], transactions["amount"], transactions["trans_date"]):
        month_year = trans_date.strftime('%Y-%m')
        if state == "approved":
            dic[(month_year, country)][0] += 1
            dic[(month_year, country)][1] += 1
            dic[(month_year, country)][2] += amount
            dic[(month_year, country)][3] += amount
        else:
            dic[(month_year, country)][0] += 1
            dic[(month_year, country)][2] += amount

    month = []
    country = []
    trans_count = []
    approved_count = []
    trans_total_amount = []
    approved_total_amount = []

    for item, val in dic.items():
        month.append(item[0])
        country.append(item[1])
        trans_count.append(val[0])
        approved_count.append(val[1])
        trans_total_amount.append(val[2])
        approved_total_amount.append(val[3])

    return pd.DataFrame({
        "month": month,
        "country": country,
        "trans_count": trans_count,
        "approved_count": approved_count,
        "trans_total_amount": trans_total_amount,
        "approved_total_amount": approved_total_amount
    })
