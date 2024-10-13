import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    dic = defaultdict(set)

    for teach, sub in zip(teacher["teacher_id"], teacher["subject_id"]):
        dic[teach].add(sub)


    teacher = []
    sub_count = []
    for item, val in dic.items():
        teacher.append(item)
        sub_count.append(len(dic[item]))

    return pd.DataFrame({"teacher_id": teacher, "cnt": sub_count})
