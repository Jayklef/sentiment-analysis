# Twitter Sentiment Classifier  

This project is a small end-to-end pipeline I built to analyze synthetic Twitter data and measure sentiment in tweets. It takes in raw tweet text with engagement metrics, processes the text to classify positivity/negativity, and then outputs structured results that can be visualized in tools like Excel or Google Sheets.  

---

## Project Overview  
The dataset I worked with contained:  
- **Tweet text**  
- **Number of retweets**  
- **Number of replies**  

I also had two word lists:  
- `positive_words.txt` → a list of words expressing positive sentiment.  
- `negative_words.txt` → a list of words expressing negative sentiment.  

The goal was to **score each tweet** based on how positive or negative it is and then analyze how sentiment correlates with engagement (e.g., retweets).  

---

## Steps I Took  

### 1. Text Preprocessing  
I started by writing a function called **`strip_punctuation`** to clean up the tweet text. This function removes punctuation marks from words so that word matching works consistently (e.g., `"happy!"` becomes `"happy"`).  

### 2. Positive Word Scoring  
I created a function **`get_pos`** that:  
- Takes in a string of tweet text.  
- Splits it into words, normalizes to lowercase, and compares against the `positive_words` list.  
- Counts how many words matched and returns a **positive score**.  

### 3. Negative Word Scoring  
Similarly, I built a function **`get_neg`** that:  
- Processes tweet text.  
- Counts occurrences of words in the `negative_words` list.  
- Returns a **negative score**.  

### 4. Sentiment Classification & Data Export  
Finally, I wrote the main processing loop that:  
- Opens the input file `project_twitter_data.csv`.  
- For each tweet, calculates:  
  - **Positive Score**  
  - **Negative Score**  
  - **Net Score** = Positive Score – Negative Score  
- Collects all results into a new CSV file called **`resulting_data.csv`**.  

The output file contains the following columns:  

| Number of Retweets | Number of Replies | Positive Score | Negative Score | Net Score |  
|---------------------|------------------|----------------|----------------|-----------|  

---

## Visualization  
Once the processed data was generated, I uploaded it into Google Sheets (or Excel) and built a chart of **Net Score vs Number of Retweets**. This provided a quick way to explore whether tweets with more positive sentiment tended to earn more engagement.  

---

## Key Takeaways  
- Learned how to **combine text processing with data analysis**.  
- Built a mini **sentiment classifier** from scratch using word lists.  
- Exported results into a structured dataset and generated insights through visualization.  

---

✅ **End result**: A working sentiment analysis tool for tweets that outputs clean data and supports quick visualization of sentiment vs engagement.  
