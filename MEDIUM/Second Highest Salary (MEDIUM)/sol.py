import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee.sort_values(by="salary", ascending=False, inplace=True)
    employee.drop_duplicates()
    highest = employee["salary"].iloc[0]

    for i, sal in enumerate(employee["salary"]):
        if sal < highest:
            return pd.DataFrame({"SecondHighestSalary": [sal]})

    return pd.DataFrame({"SecondHighestSalary": [None]})
