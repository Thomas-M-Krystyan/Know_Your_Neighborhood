#!/usr/bin/env python
import os
import sys

# Modules of the current program.
import data_manager
import ui


def separator():
    print("-" * 70)


def main():
    """
    Handle the functionality of the program.
    Support the selectable menu with an options.
    """
    os.system("clear")
    print(ui.print_menu())

    while True:
        separator()
        choice = input("Choose an option: ")

        if choice == "1":
            os.system("clear")
            separator()

        elif choice == "2":
            os.system("clear")
            separator()

        elif choice == "3":
            os.system("clear")
            separator()

        elif choice == "4":
            os.system("clear")
            separator()

        elif choice == "5":
            os.system("clear")
            separator()

        # SECRET OPTION: Display the full content table in the console.
        elif choice == "666":
            os.system("clear")

            headers = ["Województwo", "Powiat", "Gmina", "Rodzaj gminy", "Nazwa", "Typ"]

            file_content = data_manager.csv_reader("malopolska.csv")
            print(ui.print_table(headers, file_content))

        # Exit from the program.
        elif choice == "0":
            separator()
            sys.exit()

        else:
            os.system("clear")
            separator()
            print("Wrong number or invalid sign!\nPlease type the proper number")
            separator()
            print(ui.print_menu())

if __name__ == "__main__":
    main()

    # Automaticly convert the content from the file to the list of objects.
    file_content = data_manager.csv_reader("malopolska.csv")
    data_manager.table_converter(file_content)
