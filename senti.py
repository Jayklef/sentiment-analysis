import csv


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(word):

      for char in punctuation_chars:
        word = word.replace(char, "")  # remove each punctuation character
      return word



# list of positive words to use
positive_words = []
with open("assets/positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

# YOUR CODE HERE

def get_pos(text):
    count = 0
    # Convert text to lowercase
    text = text.lower()
    # Split text into words
    words = text.split()
    # Check each word
    for word in words:
        cleaned_word = strip_punctuation(word)  # remove punctuation
        if cleaned_word in positive_words:
            count += 1
    return count



# list of negative words to use
negative_words = []
with open("assets/negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

# YOUR CODE HERE

def get_neg(text):
    count = 0
    # Convert text to lowercase
    text = text.lower()
    # Split text into words
    words = text.split()
    # Check each word
    for word in words:
        cleaned_word = strip_punctuation(word)  # remove punctuation
        if cleaned_word in negative_words:
            count += 1
    return count



# Open the input CSV file
with open("assets/project_twitter_data.csv", "r") as infile:
    reader = csv.reader(infile)
    header = next(reader)  # Skip the header row
    
    # Prepare a list to store the processed rows
    processed_data = []
    
    # Process each row in the CSV
    for row in reader:
        tweet_text = row[0]               # Text of the tweet
        retweets = int(row[1])            # Number of retweets
        replies = int(row[2])             # Number of replies
        
        # Calculate positive, negative, and net scores
        pos_score = get_pos(tweet_text)
        neg_score = get_neg(tweet_text)
        net_score = pos_score - neg_score
        
        # Append the processed data
        processed_data.append([retweets, replies, pos_score, neg_score, net_score])

# Write the results to a new CSV file
with open("resulting_data.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    # Write header
    writer.writerow(["Number of Retweets", "Number of Replies", "Positive Score", "Negative Score", "Net Score"])
    # Write data rows
    writer.writerows(processed_data)

print("resulting_data.csv has been created successfully!")