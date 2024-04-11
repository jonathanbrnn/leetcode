import os

def count_folders(directory):
    folder_count = 0
    for item in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, item)):
            folder_count += 1
    return folder_count


# Example usage:
path = "../leetcode/"
total_folders = count_folders(path)
print("Total folders in the path:", total_folders)
