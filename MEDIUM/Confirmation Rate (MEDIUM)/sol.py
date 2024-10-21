import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(signups, confirmations, on='user_id', how='left')

    total_signups = merged.groupby("user_id").size()
    confirmed_signups = merged[merged["action"] == "confirmed"].groupby("user_id").size()
    confirmed_signups = confirmed_signups.reindex(total_signups.index, fill_value=0)

    confirmation_rate = (confirmed_signups / total_signups).round(2)

    return pd.DataFrame({
        "user_id": total_signups.index,
        "confirmation_rate": confirmation_rate.values
    })
