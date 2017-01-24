import shutil
import random
import datetime


class Color:
    """
    Colors and font styles for text formatting.
    """
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    END = "\033[0m"


def separator():
    """
    Decorative function to separate lines in the command console.
    Lenght of the line is calculated on the base of CLI's screen size.
    """
    cli_width = shutil.get_terminal_size()[0]  # [0] = width, [1] = height.
    print("-" * cli_width)


def print_menu():
    main_menu = """
    What would you like to do:

    (1) List statistics
    (2) Display 3 cities with longest names
    (3) Display county's name with the largest number of communities
    (4) Display locations, that belong to more than one category
    (5) Advanced search
    (0) Exit program
    """

    return main_menu


def print_table(headers, table_rows):
    """
    Function which is used to display dynamic table in the console.

    Args:
        headers (list[0]), table data (list[n+1])

    Return:
        dynamic table of strings
    """
    # Creating the dynamic table (if there is at least one row in it).
    if len(table_rows) > 0:

        # Count a length of the headers line.
        column_length = []
        # Count the amount of all headers.
        number_of_headers = 0

        for one_header in headers:
            column_length.append(len(one_header))
            number_of_headers += 1

        # Count a length of the row in the table.
        for row in table_rows:
            for element_number, element in enumerate(row):
                # Compare the longest word in the current column (headers vs. content).
                if len(str(element)) > column_length[element_number]:
                    column_length[element_number] = len(str(element))

        # Count a length of the special separator variable "width" for dynamic resizing the table.
        width = 0

        for word_length in column_length:
            width = width + word_length + 3

        # Return first line (separator) of the table.
        first_line = "." + "".rjust(width - 1, "-") + ".\n"

        # Return headers for the table.
        header_content = []

        for element_number, element in enumerate(headers):
            headers_line = "|{:^{}}".format(element, column_length[element_number] + 2)
            header_content.append(headers_line)
        end_headers_line = "|"
        header_content.append(end_headers_line)

        # Return end line (separator) after headers.
        header_separator_line = "\n|" + "".rjust(width - 1, "-") + "|\n"
        header_content.append(header_separator_line)

        # Return data content for the table.
        table_content = []
        # Count the amount of all rows in the table.
        number_of_items = 0

        for row_number, row in enumerate(table_rows, 1):
            for element_number, element in enumerate(row):
                table_line = "|{:^{}}".format(element, column_length[element_number] + 2)
                next_line = "|\n"
                table_content.append(table_line)
                number_of_items += 1
            table_content.append(next_line)

            # Return separator line for the table.
            if row_number < len(table_rows):
                end_line = "|" + "".rjust(width - 1, "-") + "|\n"
                table_content.append(end_line)

            # Return end line for the table.
            else:
                end_line = "\'" + "".rjust(width - 1, "-") + "'\n"
                table_content.append(end_line)

        # Display the sum of all items(columns) in the table.
        summary = number_of_items // number_of_headers

        # CONTENT FOR THE DYNAMIC TABLE.
        data = first_line + "".join(header_content) + "".join(table_content) + "\nNumber of all items: {}".format(summary)

        return data

    # Error handling for the empty table.
    else:
        raise ValueError("The table is empty!")


def random_greetings():
    """
    Generate random text messages at the end of the program.
    Add current time (HH:MM:SS) to the end text messages.

    Returns:
        string-type value
    """
    # Generate text message.
    greeting = random.randint(1, 3)
    # Get the actual time.
    now = datetime.datetime.now()

    if greeting == 1:
        exit_data = "Thank you for using!"

        return exit_data

    elif greeting == 2:
        exit_data = "Exit of the program at {}:{}:{}".format(now.hour, now.minute, now.second)

        return exit_data

    elif greeting == 3:
        exit_data = "Program shutdown at {}:{}:{}".format(now.hour, now.minute, now.second)

        return exit_data
