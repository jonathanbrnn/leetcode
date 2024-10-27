import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    res = []
    emp = {}

    for _id, salary in zip(employee["id"], employee["salary"]):
        emp[_id] = salary

    for _id, name, salary, managerId in zip(employee["id"], employee["name"], employee["salary"], employee["managerId"]):
        print(_id, name, salary, managerId)
        if pd.isna(_id):
            pass
        elif managerId in emp:
            if salary > emp[managerId]:
                res.append(name)

    return pd.DataFrame({"Employee": res})
