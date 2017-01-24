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

        if choice == "1":
            os.system("clear")
            ui.separator()

            header = ["No.", "MAŁOPOLSKIE"]

            received_data = LocationList().list_statistics()

            print(ui.print_center_table(header, received_data))
            ui.separator()
            print(ui.print_menu())

        elif choice == "2":
            os.system("clear")
            ui.separator()

        elif choice == "3":
            os.system("clear")
            ui.separator()

        elif choice == "4":
            os.system("clear")
            ui.separator()

        elif choice == "5":
            os.system("clear")
            ui.separator()

        # SECRET OPTION: Display the full content of the dynamic table in the console.
        elif choice == "6":
            os.system("clear")

            headers = ["Województwo", "Powiat", "Gmina", "Rodzaj gminy", "Nazwa", "Typ"]

            print(ui.print_center_table(headers, raw_file_content))

        # Exit from the program with a random greetings.
        elif choice == "0":
            ui.separator()
            print(ui.random_greetings())
            ui.separator()
            sys.exit()

        else:
            os.system("clear")
            ui.separator()
            print(ui.Color.RED + "Wrong number or invalid sign!\nPlease type the proper number" + ui.Color.END)
            ui.separator()
            print(ui.print_menu())

if __name__ == "__main__":
    # 1st step: Invoke reading the content from the following CSV file.
    raw_file_content = data_manager.csv_reader("malopolska.csv")
    # 2nd step: Invoke converting the file's content to the list of objects.
    data_manager.table_converter(raw_file_content)

    main()
