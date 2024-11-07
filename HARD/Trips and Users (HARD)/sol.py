# This is the 500th LeetCode problem I've solved!!

import pandas as pd

def save_rounding(pair):
    return round(pair[1] / pair[0], 2) if pair[1] != 0 and pair[0] != 0 else 0

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    banned = set()
    dates_seen = set()

    first = [0, 0]
    second = [0, 0]
    third = [0, 0]

    for _id, ban in zip(users["users_id"], users["banned"]):
        if ban == "Yes":
            banned.add(_id)

    for client, driver, status, date in zip(trips["client_id"], trips["driver_id"], trips["status"], trips["request_at"]):

        if client in banned or driver in banned:
            continue

        else:
            match date:
                case "2013-10-01":
                    dates_seen.add("2013-10-01")
                    first[0] += 1

                    if str(status)[:9] == "cancelled":
                        first[1] += 1

                case "2013-10-02":
                    dates_seen.add("2013-10-02")
                    second[0] += 1

                    if str(status)[:9] == "cancelled":
                        second[1] += 1

                case "2013-10-03":
                    dates_seen.add("2013-10-03")
                    third[0] += 1

                    if str(status)[:9] == "cancelled":
                        third[1] += 1

    first = save_rounding(first)
    second = save_rounding(second)
    third = save_rounding(third)

    dates = []
    cancellations = []

    if "2013-10-01" in dates_seen:
        dates.append("2013-10-01")
        cancellations.append(first)

    if "2013-10-02" in dates_seen:
        dates.append("2013-10-02")
        cancellations.append(second)

    if "2013-10-03" in dates_seen:
        dates.append("2013-10-03")
        cancellations.append(third)

    return pd.DataFrame({"Day": dates, "Cancellation Rate": cancellations})
