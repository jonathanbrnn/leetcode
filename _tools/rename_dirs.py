import os
import json

def load_problems(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def rename_dirs(file_path, difficulties):
    for subdir in os.listdir(file_path):
        subdir_path = os.path.join(file_path, subdir)
        if os.path.isdir(subdir_path):
            difficulty = difficulties.get(subdir)
            if difficulty:
                new_dir_name = f"{subdir} ({difficulty.upper()})"
                new_dir_path = os.path.join(file_path, new_dir_name)
                os.rename(subdir_path, new_dir_path)
            elif "(EASY)" not in subdir and "(MEDIUM)" not in subdir and "(HARD)" not in subdir:
                print(f"Difficulty not found for {subdir}")

if __name__ == "__main__":
    difficulties = load_problems("/Users/jonathan/PycharmProjects/leetcode/_data/difficulties.json")
    directory_path = "/Users/jonathan/PycharmProjects/leetcode/"
    rename_dirs(directory_path, difficulties)
