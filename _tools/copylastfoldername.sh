#!/bin/bash

# Specify the directory
directory="/Users/jonathan/PycharmProjects/leetcode/"

# Get the name of the last added folder
last_folder=$(ls -t -d "$directory"/*/ | head -n 1)

# Extract only the folder name
folder_name=$(basename "$last_folder")

# Copy the folder name to the clipboard
echo -n "$folder_name" | pbcopy

# Notify the user
echo "Copied '$folder_name', from the leetcode directory to the clipboard."
