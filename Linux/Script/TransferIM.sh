#!/bin/bash

###############################################################################

# Hardcoded credentials (modify these as needed)
remote_host="example.com"
username="your_username"
password="your_password"
remote_dir="/path/to/remote/directory"
filename="your_file.txt"
local_dest="/path/to/local/destination"
###############################################################################

# Generate full remote file path
remote_file="${remote_dir%/}/${filename}"
###############################################################################

# Generate new filename with date
current_date=$(date +%Y-%m-%d-%H-%M-%S)
base_name=$(basename "$filename")
new_filename="${base_name%.*}_${current_date}.${filename##*.}"
local_file="${local_dest%/}/${new_filename}"
###############################################################################

# Check if remote file exists
if ! sshpass -p "$password" ssh -o StrictHostKeyChecking=no "$username@$remote_host" "test -e '$remote_file'"; then
    echo "Error: Remote file does not exist: $remote_file"
    exit 1
fi
###############################################################################

# Check if local destination directory exists
if [ ! -d "$local_dest" ]; then
    echo "Error: Local destination directory does not exist: $local_dest"
    exit 1
fi
###############################################################################

# Get remote file details (size and modification time)
remote_file_details=$(sshpass -p "$password" ssh -o StrictHostKeyChecking=no "$username@$remote_host" "stat -c '%s %Y' '$remote_file'")
remote_file_size=$(echo "$remote_file_details" | awk '{print $1}')
remote_file_mtime=$(echo "$remote_file_details" | awk '{print $2}')
###############################################################################

# Check if local file exists and get its details
if [ -e "$local_file" ]; then
    local_file_size=$(stat -c '%s' "$local_file")
    local_file_mtime=$(stat -c '%Y' "$local_file")
###############################################################################
    # Compare remote and local files
    if [ "$remote_file_size" -eq "$local_file_size" ] && [ "$remote_file_mtime" -eq "$local_file_mtime" ]; then
        echo "No changes detected. Skipping file transfer."
        exit 0
    else
        echo "Changes detected in remote file. Proceeding with transfer..."
    fi
else
    echo "Local file does not exist. Proceeding with transfer..."
fi
###############################################################################

# Perform the file transfer
echo "Transferring file from $remote_file to $local_file..."
sshpass -p "$password" scp -o StrictHostKeyChecking=no "$username@$remote_host:'$remote_file'" "$local_file"
###############################################################################

# Verify transfer
if [ $? -eq 0 ] && [ -f "$local_file" ]; then
    echo "File successfully transferred and renamed to: $local_file"
else
    echo "Error: File transfer failed"
    exit 1
fi