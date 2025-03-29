"""
The main Python module that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""

from metrics import average, maximum, standard_deviation
from cleaner import filter_nondigits

import matplotlib.pyplot as plt


def run(filename: str) -> None:
    """
    Process heart rate data from the specified file, clean it, calculate metrics,
    and save visualizations.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, max, and standard deviation
    """ 
    data = []

    # open file using file I/O and read it into the `data` list
    book_File = open(filename)

    for line in book_File:
        data.append(line)
    
    # print(data)
    book_File.close()

    # Use `filter_nondigits` to clean the data and remove invalid entries, save the output to a new variable
    newData = filter_nondigits(data)

    # plot this data to explore changes in heart rate for this file, save this visualization to the "images" folder
    heartRate ,func = plt.subplots()

    func.plot(newData)
    func.set_title("Heart Rate Analysis")
    func.set_xlabel("x-axis")
    func.set_ylabel("y-axis")

    heartRate.savefig("")

    # calculate the average, maximum, and standard deviation of this file using the functions you've wrote
    avg_hr = average(newData)
    max_hr = maximum(newData)
    std_dev_hr = standard_deviation(newData)

    # return all 3 values
    return avg_hr, max_hr, std_dev_hr


if __name__ == "__main__":
    print(run("data/phase3.txt"))
