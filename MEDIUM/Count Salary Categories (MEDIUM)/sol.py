import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low = 0
    avg = 0
    high = 0

    for salary in accounts["income"]:
        if salary < 20000:
            low += 1
        elif salary > 50000:
            high += 1
        else:
            avg += 1

    return pd.DataFrame({"category": ["Low Salary", "Average Salary", "High Salary"], "accounts_count": [low, avg, high]})
