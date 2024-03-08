import os
import csv

# Specify the directory containing your text files
directory = 'data'  # Replace 'your_directory' with the path to your directory

# Initialize a list to store the filename and line count
results = []

# Iterate over each file in the directory
for filename in os.listdir(directory):
    # Construct the full path to the file
    file_path = os.path.join(directory, filename)
    
    # Check if the path is a file and not a directory
    if os.path.isfile(file_path):
        # Open the file and count the lines
        with open(file_path, 'r', encoding='utf-8') as file:
            line_count = sum(1 for line in file)
        
        # Append the filename and line count to the results list
        results.append((filename, line_count))

# Specify the path for the CSV file to save the results
linecountfile = 'line_counts.csv'

# Write the results to the CSV file
with open(linecountfile, 'w', newline='') as f:
    # Create a CSV writer object
    writer = csv.writer(f)
    
    # Write the header
    writer.writerow(['Filename', 'Line Count'])
    
    # Write the filename and line count for each file
    for filename, line_count in results:
        writer.writerow([filename, line_count])

print("Line counts have been saved to:", linecountfile)
