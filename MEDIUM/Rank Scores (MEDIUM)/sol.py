import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores.sort_values(by="score", ascending=False, inplace=True)

    curr_rank = 1
    last_place_value = -1
    scores_list = []
    ranks = []

    for score in scores["score"]:
        if last_place_value == -1 or last_place_value == score:
            last_place_value = score
            scores_list.append(score)
            ranks.append(curr_rank)
        elif last_place_value > score:
            curr_rank += 1
            last_place_value = score
            scores_list.append(score)
            ranks.append(curr_rank)

    return pd.DataFrame({"score": scores_list, "rank": ranks})
