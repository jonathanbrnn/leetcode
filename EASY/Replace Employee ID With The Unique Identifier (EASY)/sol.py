import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    ids = {}

    for _id, uni in zip(employee_uni["id"], employee_uni["unique_id"]):
        ids[_id] = uni

    uni_ids = []
    names = []

    for _id, name in zip(employees["id"], employees["name"]):
        if _id in ids:
            uni_ids.append(ids[_id])
        else:
            uni_ids.append(None)

        names.append(name)

    return pd.DataFrame({"unique_id": uni_ids, "name": names})
