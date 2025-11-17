base_directory="/Users/jonathan/PycharmProjects/leetcode/"
difficulty_dirs=("EASY" "MEDIUM" "HARD")

latest_folder=""
latest_folder_time=0

for difficulty in "${difficulty_dirs[@]}"; do
    difficulty_directory="$base_directory/$difficulty"

    if [ -d "$difficulty_directory" ]; then
        for folder in "$difficulty_directory"/*/; do
            folder_time=$(stat -f %m "$folder")

            if [ "$folder_time" -gt "$latest_folder_time" ]; then
                latest_folder_time=$folder_time
                latest_folder=$folder
            fi
        done
    else
        echo "Directory '$difficulty_directory' does not exist."
    fi
done

if [ -n "$latest_folder" ]; then
    folder_name="${latest_folder%/}"
    folder_name="${folder_name##*/}"
    echo "$folder_name" | pbcopy
    echo "Copied '$folder_name' to the clipboard."
else
    echo "No folders found in the difficulty directories."
fi
