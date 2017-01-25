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

    GREY_AREA = "\x1b[0;30;47m"

    END = "\033[0m"


def separator():
    """
    Decorative function to separate lines in the command console.
    Lenght of the line is calculated on the base of CLI's screen size.
    """
    cli_width = shutil.get_terminal_size()[0]  # [0] = width of terminal, [1] = height of terminal.
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


# def create_delimiters():

#     first_separator_line = []

#     first_separator_line.append(".")
#     for separator_number, separator_length in enumerate(column_length):
#         if separator_number < len(headers) - 1:
#             regular_column = "".rjust(column_width[separator_number] + 1, "-")
#             first_separator_line.append(regular_column)
#         else:
#             last_column = "".rjust(column_width[separator_number], "-") + ".\n"
#             first_separator_line.append(last_column)


def print_table(headers, table_rows, header_delimiter="|", first_align="^", second_align="^", center_align_space=2, left_space_1=0, left_space_2=0, right_space_1=0, right_space_2=0):
    """
    Function which is used to display dynamic table in the console.

    Args:
        headers (list[0]), table data (list[n+1])

    Return:
        dynamic table of strings
    """
    # Create the dynamic table (if there is at least one row in it).
    if table_rows:

        # Count a length of the headers line.
        column_length = []
        # Count the amount of all headers.
        number_of_headers = 0

        for one_header in headers:
            column_length.append(len(one_header))
            number_of_headers += 1

        # Count a length of the row in the table.
        for row in table_rows:
            for content_number, content in enumerate(row):
                # Compare the longest word in the current column (headers vs. content).
                if len(str(content)) > column_length[content_number]:
                    column_length[content_number] = len(str(content))

        # Count a length of the special separator variable "width" for dynamic resizing the table.
        width = 0
        column_width = []

        for word_length in column_length:
            column_width.append(word_length + 2)

        # NOTE [1st DATA ELEMENT]: Display the FIRST header's separator line before the headers.
        first_separator_line = []

        first_separator_line.append(".")
        for separator_number, separator_length in enumerate(column_length):
            if separator_number < len(headers) - 1:
                regular_column = "".rjust(column_width[separator_number] + 1, "-")
                first_separator_line.append(regular_column)
            else:
                last_column = "".rjust(column_width[separator_number], "-") + ".\n"
                first_separator_line.append(last_column)

        # NOTE [2nd DATA ELEMENT]: Display the headers for the table.
        table_header = []

        table_header.append("|")
        for element_number, element in enumerate(headers):
            # Print the "header_delimiter" from the function's keyword parameter (by default: "|").
            if element_number < len(headers) - 1:
                headers_line = Color.GREY_AREA + "{ls}{:{al}{len}}{rs}".format(element, al=first_align, len=column_length[element_number] + center_align_space, ls=" " * left_space_1, rs=" " * right_space_1) + Color.END + header_delimiter
                table_header.append(headers_line)
            else:
                headers_line = Color.GREY_AREA + "{ls}{:{al}{len}}{rs}".format(element, al=second_align, len=column_length[element_number] + center_align_space, ls=" " * left_space_2, rs=" " * right_space_2) + Color.END + "|\n"
                table_header.append(headers_line)

        # NOTE [3rd DATA ELEMENT]: Display the END header's separator line after the headers.
        header_separator_line = []

        header_separator_line.append("|")
        for separator_number, separator_length in enumerate(column_length):
            # Print the column delimiter (by default: "+").
            if separator_number < len(headers) - 1:
                regular_column = "".rjust(column_width[separator_number], "-") + "+"
                header_separator_line.append(regular_column)
            else:
                last_column = "".rjust(column_width[separator_number], "-") + "|\n"
                header_separator_line.append(last_column)

        # NOTE [4th DATA ELEMENT]: Display the data content for the table.
        table_content = []
        # Count the amount of all rows in the table.
        number_of_items = 0

        for row_number, row in enumerate(table_rows, 1):
            table_content.append("|")
            for element_number, element in enumerate(row):
                # Print the content delimiter (by default: "|").
                if element_number < len(headers) - 1:
                    content_line = "{ls}{:{al}{len}}{rs}".format(element, al=first_align, len=column_length[element_number] + center_align_space, ls=" " * left_space_1, rs=" " * right_space_1) + "|"
                    table_content.append(content_line)
                    number_of_items += 1
                else:
                    content_line = "{ls}{:{al}{len}}{rs}".format(element, al=second_align, len=column_length[element_number] + center_align_space, ls=" " * left_space_2, rs=" " * right_space_2) + "|\n"
                    table_content.append(content_line)
                    number_of_items += 1

            # Display the MIDDLE content's separator line after the middle content row(s).
            if row_number < len(table_rows):
                table_content.append("|")
                for separator_number, separator_length in enumerate(column_length):
                    # Print the column delimiter (by default: "+").
                    if separator_number < len(headers) - 1:
                        regular_column = "".rjust(column_width[separator_number], "-") + "+"
                        table_content.append(regular_column)
                    else:
                        last_column = "".rjust(column_width[separator_number], "-") + "|\n"
                        table_content.append(last_column)

            # Display the END content's separator line after the last content row.
            else:
                table_content.append("'")
                for separator_number, separator_length in enumerate(column_length):
                    if separator_number < len(headers) - 1:
                        regular_column = "".rjust(column_width[separator_number] + 1, "-")
                        table_content.append(regular_column)
                    else:
                        last_column = "".rjust(column_width[separator_number], "-") + "'\n"
                        table_content.append(last_column)

        # NOTE [5th DATA ELEMENT]: Display the sum of all items (rows) in the table.
        summary = number_of_items // number_of_headers

        # Create data from all the elements of above.
        data = "".join(first_separator_line) + "".join(table_header) + "".join(header_separator_line) + "".join(table_content) + "\nNumber of all items: {}".format(summary)

        return data

    # Error handling for the empty table.
    else:
        error_message = Color.RED + "ERROR: The table is empty!\nPlease check the CSV file" + Color.END

        return error_message


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
        exit_data = "MESSAGE: Thank you for using!"

        return exit_data

    elif greeting == 2:
        exit_data = "MESSAGE: Exit of the program at {}:{}:{}".format(now.hour, now.minute, now.second)

        return exit_data

    elif greeting == 3:
        exit_data = "MESSAGE: Program shutdown at {}:{}:{}".format(now.hour, now.minute, now.second)

        return exit_data
