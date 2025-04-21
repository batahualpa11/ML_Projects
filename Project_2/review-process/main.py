from label import get_sentiment
from visualize import make_plot

import json


def run(filepath: str) -> list:
    """
    Processes reviews from a JSON file, performs sentiment analysis, and creates a visualization.
    
    Args:
        filepath (str): Path to the JSON file containing reviews
        
    Returns:
        list: A list of sentiment labels for each review
    """
    # open the json object
    with open(filepath) as file:
        data = json.load(file)
    
    # extract the reviews from the json file

    reviews = data["results"][0:50]

    # reviews = data["results"][0:20]

    # for review in reviews:
    #     print(review)

    # get a list of sentiments for each line using get_sentiment
    sentiments = get_sentiment(reviews)
    
    # plot a visualization expressing sentiment ratio
    make_plot(sentiments)
    
    # return sentiments
    return sentiments


if __name__ == "__main__":
    print(run("data/raw/reviews.json"))
