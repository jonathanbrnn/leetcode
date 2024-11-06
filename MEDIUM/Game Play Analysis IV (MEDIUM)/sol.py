import pandas as pd

def is_next_day(date1: str, date2: str) -> bool:

    date1 = date1.replace("00:00:00", "")
    date2 = date2.replace("00:00:00", "")

    days_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year1, month1, day1 = map(int, date1.split("-"))
    year2, month2, day2 = map(int, date2.split("-"))

    if (year1 % 4 == 0 and year1 % 100 != 0) or year1 % 400 == 0:
        days_per_month[2] += 1

    if year1 == year2 and month1 == month2 and day2 - day1 == 1:
        return True
    elif year1 == year2 and month2 - month1 == 1 and day1 == days_per_month[month1] and day2 == 1:
        return True
    elif year2 - year1 == 1 and month1 == 12 and month2 == 1 and day1 == 31 and day2 == 1:
        return True

    return False


def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    indv = set()
    checked = set()
    logins = {}
    consecutives = 0

    activity.sort_values(by="event_date", inplace=True)

    for player, date in zip(activity["player_id"], activity["event_date"]):
        indv.add(player)

        if player not in logins:
            logins[player] = date
        elif player not in checked:
            if is_next_day(str(logins[player]), str(date)):
                consecutives += 1
            checked.add(player)

    return pd.DataFrame({"fraction": [round(consecutives / len(indv), 2)]})
