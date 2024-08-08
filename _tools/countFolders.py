import os

def count_folders(path_easy, path_medium, path_hard):
    folder_count = 0
    easy = 0
    medium = 0
    hard = 0

    for root, dirs, files in os.walk(path_easy):
        folder_count += len(dirs)
        easy += len(dirs)

    for root, dirs, files in os.walk(path_medium):
        folder_count += len(dirs)
        medium += len(dirs)

    for root, dirs, files in os.walk(path_hard):
        folder_count += len(dirs)
        hard += len(dirs)

    return folder_count, easy, medium, hard


path_easy = "/Users/jonathan/PycharmProjects/leetcode/EASY"
path_medium = "/Users/jonathan/PycharmProjects/leetcode/MEDIUM"
path_hard = "/Users/jonathan/PycharmProjects/leetcode/HARD"
total_folders, easy, medium, hard = count_folders(path_easy, path_medium, path_hard)
print("Total problems solved:", total_folders)
print("Total (EASY):", easy)
print("Total (MEDIUM):", medium)
print("Total (HARD):", hard)
