
import csv
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize the VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Specify the input and output file paths
input_file = 'data/urges.txt'
output_file = 'data/sentiment/urges.csv'

# Open the input file for reading and output file for writing
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    # Create a CSV writer object for the output file
    writer = csv.writer(outfile)
    
    # Write the header row to the output CSV file
    writer.writerow(['Line', 'Compound Sentiment Score', 'Positive Sentiment Score', 'Negative Sentiment Score', 'Neutral Sentiment Score'])
    
    # Iterate over each line in the input file
    for line in infile:
        # Perform VADER sentiment analysis on the line
        scores = sid.polarity_scores(line)
        
        # Extract sentiment scores
        compound_score = scores['compound']
        positive_score = scores['pos']
        negative_score = scores['neg']
        neutral_score = scores['neu']
        
        # Write the line and sentiment scores to the CSV file
        writer.writerow([compound_score, positive_score, negative_score, neutral_score, line.strip()])

print(f"Sentiment analysis results have been saved to {output_file}")