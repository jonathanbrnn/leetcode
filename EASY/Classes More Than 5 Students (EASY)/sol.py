import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    dic = defaultdict(set)

    for student, course in zip(courses["student"], courses["class"]):
        dic[course].add(student)

    res = []

    for item, val in dic.items():
        if len(val) >= 5:
            res.append(item)

    return pd.DataFrame({"class": res})
