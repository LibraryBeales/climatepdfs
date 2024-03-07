import os
import csv
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize the VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Specify the directory containing your text files
directory = 'data'  # Replace 'your_directory' with the path to your directory

# Initialize a list to store the filename and sentiment result
results = []

# Iterate over each file in the directory
for filename in os.listdir(directory):
    # Construct the full path to the file
    file_path = os.path.join(directory, filename)
    
    # Check if the path is a file and not a directory
    if os.path.isfile(file_path):
        # Open the file and read its contents
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Perform VADER sentiment analysis on the text
        scores = sid.polarity_scores(text)
        
        # Extract the separate sentiment scores
        pos_score = scores['pos']
        neg_score = scores['neg']
        neu_score = scores['neu']
        
        # Append the filename and sentiment scores to the results list
        results.append((filename, pos_score, neg_score, neu_score))

# Specify the path for the CSV file to save the results
csv_file = 'sentiment_results.csv'

# Write the results to the CSV file
with open(csv_file, 'w', newline='') as f:
    # Create a CSV writer object
    writer = csv.writer(f)
    
    # Write the header
    writer.writerow(['Filename', 'Positive Score', 'Negative Score', 'Neutral Score'])
    
    # Write the filename and sentiment scores for each file
    for filename, pos_score, neg_score, neu_score in results:
        writer.writerow([filename, pos_score, neg_score, neu_score])

print("Sentiment analysis results have been saved to:", csv_file)