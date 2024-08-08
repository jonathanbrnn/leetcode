import os

def count_folders(directory):
    folder_count = 0
    easy = 0
    medium = 0
    hard = 0

    for item in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, item)):
            if "(EASY)" in item:
                easy += 1
            elif "(MEDIUM)" in item:
                medium += 1
            elif "(HARD)" in item:
                hard += 1
            folder_count += 1

    return folder_count, easy, medium, hard


path = "/Users/jonathan/PycharmProjects/leetcode/"
total_folders, easy, medium, hard = count_folders(path)
print("Total folders in the path:", total_folders)
print("Total (EASY):", easy)
print("Total (MEDIUM):", medium)
print("Total (HARD):", hard)
