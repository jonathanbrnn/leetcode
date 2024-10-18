import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    students = []
    _id = []
    last = None

    for i, student in enumerate(seat["student"]):
        _id.append(i + 1)
        if i % 2 != 0:
            students.append(student)
            students.append(last)
        else:
            last = student

    if last not in students and last:
        students.append(last)

    return pd.DataFrame({"id": _id, "student": students})
