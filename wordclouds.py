from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

# Specify the directory containing your text files
input_directory = 'data'  # Replace 'input_directory' with the path to your directory
output_directory = 'wordclouds'  # Specify the directory to save wordcloud files

# Create the output directory if it does not exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Iterate over each file in the input directory
for filename in os.listdir(input_directory):
    # Construct the full path to the file
    file_path = os.path.join(input_directory, filename)
    
    # Check if the path is a file and not a directory, and if it's a text file
    if os.path.isfile(file_path) and filename.endswith('.txt'):
        # Read the contents of the text file
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Create a WordCloud object
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        
        # Set the word cloud title as the filename
        plt.title(filename)
        
        # Display the word cloud
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')  # Turn off axis
        
        # Save the word cloud to a file with the same name as the text file in the output directory
        wordcloud_file = os.path.splitext(filename)[0] + '_wordcloud.png'
        output_file_path = os.path.join(output_directory, wordcloud_file)
        wordcloud.to_file(output_file_path)
        print(f"Word cloud saved as {output_file_path}")
