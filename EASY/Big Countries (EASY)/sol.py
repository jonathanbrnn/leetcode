import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    large_country_names = []
    large_country_areas = []
    large_country_populations = []

    for name, area, population in zip(world["name"], world["area"], world["population"]):
        if area >= 3000000 or population >= 25000000:
            large_country_names.append(name)
            large_country_areas.append(area)
            large_country_populations.append(population)

    return pd.DataFrame({"name": large_country_names, "area": large_country_areas, "population": large_country_populations})
