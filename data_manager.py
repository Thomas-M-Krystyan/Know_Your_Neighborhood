import re

# Modules of the current program.
from statistics import *


def csv_reader(data_file_name):
    """
    Method reads CSV files and returns their content as a list of lists which contains a strings.

    Returns:
        list of lists (with strings)
    """
    file_content = []

    with open(data_file_name, "r", encoding="utf-8") as file:
        next(file)
        for line in file:
            clean_line = (re.split(',|;|:|\t|\n', line.strip()))  # Clearing every line of data list (removing separators and "\t", "\n") with RegEx.
            file_content.append(clean_line)

    return file_content


def table_converter(data_file):
    """
    Convert the content of a file (list of lists) to the list
    of objects in Voivodeship class from "statistics.py" file.

    Reference to the following elements from list:

       index:
        [0] = ID of the voivodeship
        [1] = ID of the county
        [2] = ID of the community
        [3] = ID of the type of community
        [4] = Name of the region
        [5] = Name of the region's type

    Returns:
        None
    """
    for element in data_file:
        # Create an instances of every line (row) with content from the list of lists.
        current_location = Location(element[0], element[1], element[2], element[3], element[4], element[5])

        # Deliver the already created instances to the agregation-type class "LocationList".
        LocationList().add_location(current_location)
