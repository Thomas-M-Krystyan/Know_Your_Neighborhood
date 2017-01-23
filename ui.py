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
    # Error handling for an empty table.
    if len(table_rows) == 0:
        return None

    else:
        # Count lenght of the headers line.
        column_length = []
        for element in headers:
            column_length.append(len(element))

        # Count lenght of the row in the table.
        for row in table_rows:
            for element_number, element in enumerate(row):
                # Compare the longest word in the current column (headers vs. content).
                if len(str(element)) > column_length[element_number]:
                    column_length[element_number] = len(str(element))

        # Count lenght of the special separator variable "width" for dynamic resizing the table.
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
        for row_number, row in enumerate(table_rows, 1):
            for element_number, element in enumerate(row):
                table_line = "|{:^{}}".format(element, column_length[element_number] + 2)
                next_line = "|\n"
                table_content.append(table_line)
            table_content.append(next_line)

            # Return separator line for the table.
            if row_number < len(table_rows):
                end_line = "|" + "".rjust(width - 1, "-") + "|\n"
                table_content.append(end_line)

            # Return end line for the table.
            else:
                end_line = "\'" + "".rjust(width - 1, "-") + "'\n"
                table_content.append(end_line)

        # CONTENT FOR THE TABLE.
        data = first_line + "".join(header_content) + "".join(table_content)

        return data
