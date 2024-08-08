import os
import shutil

def move_folders_by_difficulty(source_dir, dest_base_dir):
    # Define the difficulty levels
    difficulties = ['EASY', 'MEDIUM', 'HARD']

    # Ensure destination directories exist
    for difficulty in difficulties:
        dest_path = os.path.join(dest_base_dir, difficulty)
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)

    # Iterate over the folders in the source directory
    for folder in os.listdir(source_dir):
        folder_path = os.path.join(source_dir, folder)

        if os.path.isdir(folder_path):
            # Check and extract difficulty from folder name
            for difficulty in difficulties:
                if difficulty in folder:
                    # Avoid moving folders into subdirectories
                    dest_path = os.path.join(dest_base_dir, difficulty)

                    # Ensure that we're not moving a folder into itself
                    if not os.path.commonpath([folder_path, dest_path]) == dest_path:
                        shutil.move(folder_path, os.path.join(dest_path, folder))
                        print(f"Moved '{folder_path}' to '{os.path.join(dest_path, folder)}'")
                    else:
                        print(f"Skipped moving '{folder_path}' to avoid self-move.")
                    break

if __name__ == "__main__":
    source_directory = '/Users/jonathan/PycharmProjects/leetcode/'  # Source directory with current folders  # Base directory for destination folders

    move_folders_by_difficulty(source_directory, source_directory)
