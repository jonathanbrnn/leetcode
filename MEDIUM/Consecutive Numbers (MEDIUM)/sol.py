import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    stack = []
    consecutives = set()

    for num in logs["num"]:
        if len(stack) < 3:
            stack.append(num)
        else:
            if len(set(stack)) == 1:
                consecutives.add(stack[0])
            stack.pop(0)
            stack.append(num)

    if len(set(stack)) == 1 and len(logs["num"]) > 2:
        consecutives.add(stack[0])

    return pd.DataFrame({"ConsecutiveNums": list(consecutives)})
