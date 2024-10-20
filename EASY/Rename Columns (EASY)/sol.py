import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({"student_id": students["id"], "first_name": students["first"], "last_name": students["last"], "age_in_years": students["age"]})
