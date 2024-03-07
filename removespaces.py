import os

# Specify the directory path
directory = 'docs/textfiles'

# Iterate over each file in the directory
for filename in os.listdir(directory):
    # Construct the old and new filenames
    old_file_path = os.path.join(directory, filename)
    new_filename = filename.replace(' ', '')  # Remove spaces from the filename
    new_file_path = os.path.join(directory, new_filename)

    # Rename the file
    os.rename(old_file_path, new_file_path)