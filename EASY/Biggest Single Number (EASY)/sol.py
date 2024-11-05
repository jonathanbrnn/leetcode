import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    cou = Counter(list(my_numbers["num"]))
    greatest = -1

    for item, val in cou.items():
        if val == 1:
            greatest = max(greatest, item)

    return pd.DataFrame({"num": [greatest]}) if greatest != -1 else pd.DataFrame({"num": [None]})
