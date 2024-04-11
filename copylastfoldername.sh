#!/bin/bash

# Get the name of the last added folder
last_folder=$(ls -t -d */ | head -n 1)

# Copy the folder name to the clipboard
echo -n "$last_folder" | pbcopy

# Notify the user
echo "Copied '$last_folder' to the clipboard."
