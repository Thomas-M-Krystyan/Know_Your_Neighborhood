import re

# Modules of the current program.
from administrative_statistics import Voivodeship


def csv_reader(data_file_name):
    """
    Method reads CSV files and returns their content as a list of lists which contains a strings.
    """
    file_content = []
    with open(data_file_name, "r") as file:
        next(file)
        for line in file:
            clean_line = (re.split(',|\t|\n', line.strip()))  # Clearing every line of data list (removing ",", "\t", "\n") with RegEx.
            file_content.append(clean_line)

    return file_content


def table_converter(file_content):
    """
    Convert the content of a file (list of lists) to the objects ("list_of_current_location").

    Reference to the following elements from list:

       index:
        [0] = ID of the voivodeship
        [1] = ID of the county
        [2] = ID of the community
        [3] = ID of the type of community
        [4] = Name of the region
        [5] = Name of the region type

    Returns:
        list of objects
    """
    list_of_current_location = []

    for element in file_content:
        current_location = Voivodeship(element[0], element[1], element[2], element[3], element[4], element[5])
        list_of_current_location.append(current_location)

    return list_of_current_location
