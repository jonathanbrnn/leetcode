import os
import json
import random
import webbrowser

def load_problems(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

problems_file_path = "/Users/jonathan/PycharmProjects/leetcode/_data/difficulties.json"
problems = load_problems(problems_file_path)
order = {"Easy": 1, "Medium": 2, "Hard": 3}
problems = dict(sorted(problems.items(), key=lambda x: order[x[1]]))

easy_problems = []
medium_problems = []
hard_problems = []

for item, val in problems.items():
    if val == "Easy":
        easy_problems.append(item)
    elif val == "Medium":
        medium_problems.append(item)
    else:
        hard_problems.append(item)

def fetch_problem(problems):
    rand_int = random.randint(0, len(problems) - 1)
    return problems[rand_int]

problem_to_open = None
to_fetch = input()
if to_fetch == "e":
    fetch_problem(easy_problems)
elif to_fetch == "m":
    fetch_problem(medium_problems)
else:
    fetch_problem(hard_problems)
problem_to_open = problem_to_open.lower()
problem_to_open = problem_to_open.split()
problem_to_open = "-".join(problem_to_open)
print(problem_to_open)

webbrowser.open_new_tab("https://leetcode.com/problems/"+problem_to_open)
