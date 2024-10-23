import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    connections = defaultdict(set)

    for req, acc in zip(request_accepted["requester_id"], request_accepted["accepter_id"]):
        connections[req].add((req, acc))
        connections[acc].add((req, acc))

    id = None
    num = -1

    for item, val in connections.items():
        if len(val) > num:
            id = item
            num = len(val)

    return pd.DataFrame({"id": [id], "num": [num]})
