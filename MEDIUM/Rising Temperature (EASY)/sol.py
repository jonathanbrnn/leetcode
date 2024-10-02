import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather_sorted = weather.sort_values(by='recordDate')
    placeholder = []

    weather_sorted['recordDate'] = pd.to_datetime(weather_sorted['recordDate'])

    for i in range(1, len(weather_sorted)):
        if (weather_sorted.iloc[i]['recordDate'] - weather_sorted.iloc[i - 1]['recordDate']).days == 1:
            if weather_sorted.iloc[i]['temperature'] > weather_sorted.iloc[i - 1]['temperature']:
                placeholder.append(weather_sorted.iloc[i]['id'])

    res = pd.DataFrame(placeholder, columns=["id"])

    return res
