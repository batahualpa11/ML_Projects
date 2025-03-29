def average(data: list) -> float:
    """
    Calculate average value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the average of this list
    -----
    I begin by creating 3 variables (avg, total, and count) and initilize them to 0.
    The avg, total, and count variable are set to zero so it can be updated after calculation.
    A for-loop is created to iterate over the list in the variable 'data'.
    Within the for-loop I use a shorthand operator to update the total variable to based on the number in the list.
    I also update the count variable by +1 each time until the list ends.
    In line 27 I create an if statement with the condition to execute when count is equal to 0 and will return an empty list, because there is no value in the list.
    In line 28, I update the value of 'avg' to be the value after the calculation of total / count.
    In line 31, I return the calculation of average (avg) and use the round function.
    """
    avg = 0
    total = 0
    count = 0
    
    for num in data:
        total += num
        count += 1
    
    if count == 0:
        return []  
    
    avg = total / count
    return round(avg,2)


def maximum(data: list) -> float:
    """
    I created an if statement to check if the data is empty or has values.
    If false then it will return an empty list.
    If true, it will intitialize the variable max_value to the first index of the list.
    Then it will go through a for-loop and iterate through the list.
    Another if statement was implemented in the for-loop with the condition that each number is greater than the value of max_value.
    If true it would update the max_value to be the same value of the current number(num).
    """
    
    if data:  # Check if the list is not empty
        max_value = data[0]  # Initialize with the first element
        
        for num in data:  
            if num > max_value:
                max_value = num  
        return max_value
    return []



def variance(data: list) -> float:
    """
    I begin by initilizing the 'myVariance' variable to be an empty list.
    Next I create the variable mean to be the value after the calculation of sum / length of the list 'data'.
    I then proceeed a for-loop to iterate over each element in the list 'data'.
    Within the for-loop, I create a variable 'difference' to assign the value of each element subtracted by the mean and squared.
    Once the difference is calculated, I append the 'difference' to my empty list 'myVariance'.
    After I loop through all the elements, I calculate variance by dividing the sum of 'myVariance' divided by the length of the list 'data'.
    Lastly, we return 'calcVariance' which is the calculated population variance.
    """
    myVariance = []
    mean = sum(data)/len(data)

    for i in data:
        difference = (i - mean) ** 2
        myVariance.append(difference)
    
    calcVariance = sum(myVariance)/len(data)
    
    return(calcVariance)


def standard_deviation(data: list) -> float:
    """
    After viewing the potential test cases for the standard deviation function.
    I noticed that one test case was checking if there is an empty list it would return an empty list.
    If the data is not an empty list it would calculate the standard deviation by call the variance function to the power of 0.5.
    Then after completing the else statement it would print out the value of population standard deviation utilizing the round function.
    """
    if data == []:
        return[]
    else:
        standard_dev = variance(data) ** 0.5
    
    return round(standard_dev,2)
