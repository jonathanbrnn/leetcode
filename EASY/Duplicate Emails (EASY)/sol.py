import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    res = set()
    emails = set()

    for email in person["email"]:
        if email in emails:
            res.add(email)
        else:
            emails.add(email)

    return pd.DataFrame({"Email": list(res)})
