def filter_nondigits(data: list) -> list:
    """
    In the following lines starting from Line 5 - 12. 
    I've created a variable named "cleaned_Data" and intitialized it to be an empty list.
    I then proceeded to create 'for-loop' to iterate over each item in data.
    Then I assign the item variable to utilize the strip method to remove any whitespace or new lines.
    Within the 'for-loop' I created an if-statement itilizing the isDigit() method.
    Within the 'if-loop' I append each digit of int data type in item.
    Lastly I return cleaned_Data to what was an empty list. 
    """
    cleaned_Data = []

    for item in data:
        item = item.strip()

        if item.isdigit():
            cleaned_Data.append(int(item))
    return cleaned_Data


