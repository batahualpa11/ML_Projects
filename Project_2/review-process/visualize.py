import matplotlib.pyplot as plt


def make_plot(sentiments: list) -> None:
    """
    Creates a bar plot showing the count of each sentiment type and saves it to the images folder.
    
    Args:
        sentiments (list): A list of sentiment labels ("positive", "neutral", "negative", "irrelevant")
    """
    # Counting each sentiment type into integers
    counts = {
        "positive": sentiments.count("positive"),
        "neutral": sentiments.count("neutral"),
        "negative": sentiments.count("negative"),
        "irrelevant": sentiments.count("irrelevant")
    }
    
    # Create the bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(counts.keys(), counts.values())
    
    
    # Customize the plot
    plt.title('Sentiment Analysis Results')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    
    
    # Save the plot
    plt.savefig('images/sentiment_analysis.png') # Saves the plot to the images folder
    plt.close()
