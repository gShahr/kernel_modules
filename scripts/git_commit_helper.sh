#!/bin/bash

# Ask user which files to add
echo "Enter the files you want to add (space-separated), or type 'all' to add everything:"
read -r files

# If user types 'all', stage all changes
if [ "$files" == "all" ]; then
    git add .
else
    git add $files
fi

# Show staged changes
echo -e "\nStaged changes:"
git status --short

# Ask for commit title
echo -e "\nEnter commit title:"
read -r commit_title

# Ask for commit body
echo -e "\nEnter commit body (press Enter twice to finish):"
commit_body=""
while IFS= read -r line; do
    [[ -z "$line" ]] && break
    commit_body+="$line\n"
done

# Automatically wrap the commit body at 72 characters
wrapped_commit_body=$(echo -e "$commit_body" | fold -s -w 75)

# Make the commit
git commit -m "$commit_title" -m "$wrapped_commit_body"

# Generate the patch
git format-patch -1 -o ./
patch_file=$(ls -t | grep -m1 ".patch")

# Run checkpatch.pl
if [ -f "../../linux_mainline/scripts/checkpatch.pl" ]; then
    echo -e "\nRunning checkpatch.pl on $patch_file..."
    ../../linux_mainline/scripts/checkpatch.pl --strict "$patch_file"
else
    echo -e "\nWarning: checkpatch.pl script not found at ../../linux_mainline/scripts/checkpatch.pl"
fi

echo -e "\n✅ Commit and checkpatch complete!"
