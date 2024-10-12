import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if N < 1:
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})

    employee.sort_values(by="salary", ascending=False, inplace=True)
    employee.drop_duplicates(subset="salary",inplace=True)

    if len(employee) >= N:
        return pd.DataFrame({f"getNthHighestSalary({N})": [employee["salary"].iloc[N-1]]})
    return pd.DataFrame({f"getNthHighestSalary({N})": [None]})
