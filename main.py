#!/usr/bin/env python
import os
import sys

# Modules of the current program.
import data_manager
import ui
from statistics import Location, LocationList


def main():
    """
    Handle the functionality of the program.
    Support the selectable menu with an options.
    """
    os.system("clear")
    print(ui.print_menu())

    while True:
        ui.separator()
        choice = input("Choose an option: ")

        # NOTE [OPTION 1]: List statistics of the current voivodeship (by default: "Małopolskie").
        if choice == "1":
            os.system("clear")

            # Get a name of the current voivodeship from the CSV file.
            name_of_voivodeship = LocationList().voivodeship_name()

            # Initialize the headers for the dynamic table.
            header = ["", name_of_voivodeship]

            # Initialize the data for the dynamic table.
            received_data = LocationList().list_statistics()[1]

            # Initialize the summary for number of all unique locations.
            summary = LocationList().list_statistics()[0]

            # Display the table.
            print(ui.print_table(header, received_data, ui.Color.GREY_AREA + " " + ui.Color.END, ">", "<"))
            """
            .---------------------------------.
            |       MAŁOPOLSKIE               |  <--- Grey empty string (" ") delimiter before name of the voyevodeship
            |-----+---------------------------|
            | 122 | gmina wiejska             |
            |-----+---------------------------|
            |   3 | miasto na prawach powiatu |
            '---------------------------------'
                >   <                               <--- Type of the text alignment:
                                                            to the right (">") and do the left "<")
            """
            ui.separator()
            print("Number of all locations: {}".format(ui.Color.GREEN + str(summary) + ui.Color.END))
            ui.separator()
            print("* Including: \"miasto na prawach powiatu\"")
            ui.separator()
            print(ui.print_menu())

        # NOTE [OPTION 2]: Display three cities with the longest names.
        elif choice == "2":
            os.system("clear")

            # Initialize the headers for the dynamic table.
            header = ["The longest city names", "Letters"]

            # Initialize the data for the dynamic table.
            received_data = LocationList().longest_city_namess()

            # Display the table.
            print(ui.print_table(header, received_data))
            ui.separator()
            print(ui.print_menu())

        # NOTE [OPTION 3]: Display county's name with the largest number of communities.
        elif choice == "3":
            os.system("clear")

            # Initialize the headers for the dynamic table.
            header = ["The largest county", "Communities"]

            # Initialize the data for the dynamic table.
            received_data = LocationList().largest_county()

            # Display the table.
            print(ui.print_table(header, received_data))
            ui.separator()
            print(ui.print_menu())

        # NOTE [OPTION 4]: Display locations, that belong to more than one category.
        elif choice == "4":
            os.system("clear")

            # Initialize the headers for the dynamic table.
            header = ["Locations of multiple types", "Occurrences"]

            # Initialize the data for the dynamic table.
            received_data = LocationList().locations_of_multiple_types()

            # Display the table.
            print(ui.print_table(header, received_data))
            ui.separator()
            print(ui.print_menu())

        # NOTE [OPTION 5]: Advanced search for substring among the location names.
        elif choice == "5":
            os.system("clear")

            # Ask the user for the input (substring).
            searched_phrase = input("Searching for: ")

            # Initialize the headers for the dynamic table.
            header = ["LOCATION", "TYPE"]

            # Initialize the data for the dynamic table.
            received_data = LocationList().advanced_search(searched_phrase)

            # Handle the case when nothing wasn't found and prevents the broken (ugly) table.
            if received_data == []:
                received_data = [("None", "None")]

            # Display the table.
            print(ui.print_table(header, received_data, "|", "<", "<"))
            ui.separator()
            print(ui.print_menu())

        # NOTE [SECRET OPTION]: Display a full content of the dynamic table from the CSV file.
        elif choice == "6":
            os.system("clear")

            # Initialize the headers for the dynamic table.
            headers = ["Voivodeship ID", "County ID", "Community ID", "Community Type ID", "Name of Location", "Type of Location"]

            # Display the table.
            print(ui.print_table(headers, raw_file_content))  # Receive the data for the dynamic table from the "data_manager.py".
            ui.separator()
            print(ui.print_menu())

        # NOTE [OPTION 0]: Exit from the program with a random greetings.
        elif choice == "0":
            ui.separator()
            print(ui.random_greetings())
            ui.separator()
            sys.exit()

        else:
            os.system("clear")
            ui.separator()
            print(ui.Color.RED + "ERROR: Wrong number or invalid sign!\nPlease type only the proper number..." + ui.Color.END)
            ui.separator()
            print(ui.print_menu())

if __name__ == "__main__":
    # 1st step: Invoke reading the content from the following CSV file.
    raw_file_content = data_manager.csv_reader("malopolska.csv")
    # 2nd step: Invoke converting the file's content to the list of objects.
    data_manager.table_converter(raw_file_content)
    # 3rd step: Execute the main function of the program.
    main()
