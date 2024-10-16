import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    dic = defaultdict(int)

    for emp, day, in_t, out_t in zip(employees["emp_id"], employees["event_day"], employees["in_time"], employees["out_time"]):
        dic[(day, emp)] += abs(out_t - in_t)

    days = []
    emp_id = []
    total_time = []

    for item, val in dic.items():
        days.append(item[0])
        emp_id.append(item[1])
        total_time.append(val)

    return pd.DataFrame({"day": days, "emp_id": emp_id, "total_time": total_time})
