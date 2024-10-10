import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    last = ""
    current_weight = 0

    queue.sort_values(by="turn", ascending=True, inplace=True)

    for weight, name in zip(queue["weight"], queue["person_name"]):
        if current_weight + weight > 1000:
            return pd.DataFrame({"person_name": [f"{last}"]})
        elif current_weight + weight == 1000:
            return pd.DataFrame({"person_name": [f"{name}"]})
        else:
            current_weight += weight
            last = name

    return pd.DataFrame({"person_name": [f"{last}"]})
