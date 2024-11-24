import pandas as pd

def movie_rating(_movies: pd.DataFrame, _users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    users = defaultdict(int)
    movies = defaultdict(lambda: [0, 0])

    users_lookup = {}
    movies_lookup = {}

    for user_id, name in zip(_users["user_id"], _users["name"]):
        users_lookup[user_id] = name

    for movie_id, title in zip(_movies["movie_id"], _movies["title"]):
        movies_lookup[movie_id] = title

    for movie_id, user_id, rating, date in zip(movie_rating["movie_id"], movie_rating["user_id"], movie_rating["rating"], movie_rating["created_at"]):
        users[users_lookup[user_id]] += 1

        if str(date)[:7] == "2020-02":
            movies[movies_lookup[movie_id]][0] += 1
            movies[movies_lookup[movie_id]][1] += rating

    highest_rated_name = ""
    highest_rated_rating = 0

    for item, val in movies.items():
        curr_rating = round(val[1] / val[0], 2)

        if curr_rating > highest_rated_rating or (curr_rating == highest_rated_rating and item < highest_rated_name):
            highest_rated_name = item
            highest_rated_rating = curr_rating

    most_active_name = ""
    most_active_count = 0

    for item, val in users.items():
        if val > most_active_count or (users[item] == most_active_count and item < most_active_name):
            most_active_name = item
            most_active_count = val

    return pd.DataFrame({"results": [most_active_name, highest_rated_name]})
