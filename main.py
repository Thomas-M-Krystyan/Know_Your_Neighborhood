#!/usr/bin/env python
import os
import sys

# Modules of the current program.
import data_manager
import ui
from statistics import *


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

            # Get name of the current voivodeship from CSV file.
            name_of_voivodeship = LocationList().voivodeship_name()

            # Initialize the headers for the dynamic table.
            header = ["", name_of_voivodeship]

            # Initialize the data for the dynamic table.
            received_data = LocationList().list_statistics()

            print(ui.print_table(header, received_data))
            ui.separator()
            print(ui.print_menu())

        # NOTE [OPTION 2]: Display three cities with the longest names.
        elif choice == "2":
            os.system("clear")

            # Initialize the headers for the dynamic table.
            header = ["Cities: The longest name"]

            # Initialize the data for the dynamic table.
            received_data = LocationList().longest_names()

            print(ui.print_table(header, received_data))
            ui.separator()
            print(ui.print_menu())

        # NOTE [OPTION 3]:
        elif choice == "3":
            os.system("clear")
            ui.separator()

        # NOTE [OPTION 4]:
        elif choice == "4":
            os.system("clear")
            ui.separator()

        # NOTE [OPTION 5]:
        elif choice == "5":
            os.system("clear")
            ui.separator()

        # NOTE [SECRET OPTION]: Display a full content of the dynamic table from the CSV file.
        elif choice == "666":
            os.system("clear")

            # Initialize the headers for the dynamic table.
            headers = ["Voivodeship", "County", "Commune", "Type of Commune", "Name of Location", "Type of Location"]

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

    main()
