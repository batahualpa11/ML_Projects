from openai import OpenAI
client = OpenAI()


def get_sentiment(text: list) -> list:
    """
    Analyzes a list of text reviews and returns their sentiment labels.
    
    Args:
        text (list): A list of string reviews to analyze
        
    Returns:
        list: A list of sentiment labels ("positive", "neutral", "negative", "irrelevant")
              or an error message if input is invalid
    """
    
    # Check if the input is empty
    if len(text) == 0:
        return "Wrong input. text must be an array of strings."
    
    # Check if all items in the list are strings
    for item in text:
        if type(item) == str:
            continue
        else:
            return "Wrong input. text must be an array of strings."

    system_prompt = """You are an expert in analyzing customer reviews and determining sentiment.
    Your task is to categorize each review as either positive, neutral, negative, or irrelevant.
    
    Examples:
    "I love this product, it's amazing!" -> positive
    "The product is okay, nothing special" -> neutral
    "This is terrible, I want a refund" -> negative
    "I had pizza for lunch today" -> irrelevant
    """

    prompt = f""" For each line of text in the string below, please categorize the review
    as either positive, neutral, negative, or irrelevant.

    Use only a one-word response per line. Do not include any numbers.
    {text}
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "developer", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
    )

    # Get the response text
    response_text = response.choices[0].message.content
    
    # Split the response into lines
    lines = response_text.split('\n')
    
    # Clean up each line
    result = []
    for line in lines:
        # Remove any extra spaces and convert to lowercase
        clean_line = line.strip().lower()
        # Only add non-empty lines
        if clean_line:
            result.append(clean_line)
    return result