import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    logins = logins[(logins["time_stamp"] >= "2020-01-01") & (logins["time_stamp"] < "2021-01-01")]
    logins = logins.sort_values(by=["user_id", "time_stamp"], ascending=[True, False]).drop_duplicates("user_id")
    return logins[["user_id", "time_stamp"]].rename(columns={"time_stamp": "last_stamp"})
