import operator

# Modules of the current program.
import ui


class Location(object):
    """
    Parent class using for creating instances
    of the current locations from the CSV file
    (e.g. cities, towns, villages, delegatures).
    """
    def __init__(self, voivodeship_id, county_id, community_id, community_type_id, location_name, location_type):
        self.voivodeship_id = voivodeship_id
        self.county_id = county_id
        self.community_id = community_id
        self.community_type_id = community_type_id
        self.name = location_name
        self.type = location_type


class LocationList(object):
    """
    Independent class using for aggregating the instances
    of the class "Location" and for operating on them.
    """
    list_of_locations = []

    def add_location(self, current_location):
        """
        The method to append to the class attribute "list_of_locations" instances of the "Location" class.
        """
        self.list_of_locations.append(current_location)

    def voivodeship_name(self):
        """
        The method to finding the name of a current VOIVODESHIP in the CSV file.

        Returns:
            string
        """
        name_of_the_voivodeship = None

        for location in self.list_of_locations:
            # Take into consideration only the following location type: "Voivodeship".
            if location.voivodeship_id != "" and location.county_id == "":
                # Capitalize the whole name, just in case.
                name_of_the_voivodeship = location.name.upper()

        return name_of_the_voivodeship

    def list_statistics(self):
        """
        The method to count the occurrences of the specific types of locations from
        the indicated CSV file and to convert the gained data to the list of tuples.

        Returns:
            list of tuples (with strings)
        """
        # NOTE: Calculate the following statistics.
        number_of_different_counties = set()
        number_of_urban_communities = 0
        number_of_rural_communities = 0
        number_of_urban_rural_communities = 0
        number_of_villages = 0
        number_of_towns = 0
        number_of_cities = 0

        for location in self.list_of_locations:
            # Count the unique occurrences of the different "Counties".
            if location.county_id != "":  # Do not count the empty strings.
                number_of_different_counties.add(location.county_id)
                # Set the label name to the table as plural "powiaty" (instead of the original singular name "powiat").
                different_counties_name = "powiaty*"

            # Count the occurrences of the following location type: "Urban community".
            if location.community_type_id == "1":
                number_of_urban_communities += 1
                urban_communities_name = location.type

            # Count the occurrences of the following location type: "Rural community".
            if location.community_type_id == "2":
                number_of_rural_communities += 1
                rural_communities_name = location.type

            # Count the occurrences of the following location type: "Urban-rural community".
            if location.community_type_id == "3":
                number_of_urban_rural_communities += 1
                urban_rural_communities_name = location.type

            # Count the occurrences of the following location type: "Village".
            if location.community_type_id == "5":
                number_of_villages += 1
                villages_name = location.type

            # Count the occurrences of the following location type: "Town".
            if location.community_type_id == "4":
                number_of_towns += 1
                towns_name = location.type

            # Insensitiveness for uppercase letters.
            type_of_location = location.type.lower()
            # Count the occurrences of the following location type: "City with county rights".
            if type_of_location == "miasto na prawach powiatu":
                number_of_cities += 1
                cities_name = location.type

        # NOTE: Create the dictionaries from the "location.type" (name of location type) as the KEY, and count of occurrences as the VALUE.
        dict_different_counties = {different_counties_name: len(number_of_different_counties)}
        dict_urban_communities = {urban_communities_name: number_of_urban_communities}
        dict_rural_communities = {rural_communities_name: number_of_rural_communities}
        dict_urban_rural_communities = {urban_rural_communities_name: number_of_urban_rural_communities}
        dict_villages = {villages_name: number_of_villages}
        dict_towns = {towns_name: number_of_towns}
        dict_cities = {cities_name: number_of_cities}

        # NOTE: Stack the dictionaries all together in a tuple.
        tuple_of_all_dictionaries = (dict_different_counties, dict_urban_communities, dict_rural_communities,
                                     dict_urban_rural_communities, dict_villages, dict_towns, dict_cities)

        # NOTE: Save the values and keys from all of the dictionaries in the dedicated list.
        all_dictionaries_items = []

        for one_dictionary in tuple_of_all_dictionaries:
            for key, value in one_dictionary.items():
                # Add collection of string-type items as tuple to the list of tuples "all_dictionaries_items".
                all_dictionaries_items.extend([(str(value), key)])

        return all_dictionaries_items

    def longest_cities_names(self):
        """
        The method to count the name length of all the CITIES from
        the database and get the longest name (by default: top 3).

        Returns:
            list of tuples (with strings)
        """
        # NOTE: List of all dictionaries generated below.
        all_locations_names_dictionaries = []

        for location in self.list_of_locations:
            # Take into consideration only the following location type: "City".
            if location.community_type_id == "4":
                name_length = len(location.name)
                name = location.name
                # Make a dictionaries with the "name" and "name_length" of the current location as the VALUES.
                dict_location_name = {"Name": name, "Name length": name_length}
                all_locations_names_dictionaries.append(dict_location_name)

        # NOTE: Sort the gained dictionaries in DESCENDING ORDER by their keys ("Name length").
        sorted_list = sorted(all_locations_names_dictionaries, key=operator.itemgetter("Name length"), reverse=True)

        # NOTE: Get the first three longest names from the list (with the number of characters: letters, spaces and "-").
        the_longest_names = []

        for number, location in enumerate(sorted_list, 1):
            # Count only the top 3 longest city names.
            if number < 4:
                # Add values of the following keys as a tuple to the list of tuples "the_longest_names".
                the_longest_names.extend([(location.get("Name"), location.get("Name length"))])

        return the_longest_names

    def largest_county(self):
        """
        The method to find the county's name with
        the largest number of communities in it.

        Returns:
            list with tuple (with strings)
        """
        # NOTE: Create the list which contains the dictionaries of all counties in the CSV file.
        list_of_all_counties_dict = []

        for location in self.list_of_locations:
            # Take into consideration only the following location types: "County" and "City with county rights".
            if location.county_id != "" and location.community_id == "":
                # Create the dictionary for the current county based on its "county_id" and "name" as VALUES.
                list_of_all_counties_dict.append({"ID": location.county_id, "Name": location.name, "Communities": 0})  # Set the counter to 0.

        # NOTE: Count the number of individual communities of any type in the all following counties.
        for county_dict in list_of_all_counties_dict:
            # Count the occurances of any communities for the current county.
            any_type_of_community_in_county = []
            for location in self.list_of_locations:
                # Match the "ID" of the current county from "list_of_all_counties_dict" to the "county_id" of the communities in "list_of_locations".
                if location.county_id == county_dict.get("ID"):
                    # Take into consideration any type of the following communities: "Urban" (1), "Rural" (2) and "Urban-Rural" (3).
                    if location.community_type_id in ("1", "2", "3"):
                        any_type_of_community_in_county.append(location)  # Count the found communities as the objects.

            # Update the default number (0) of "Communities" for the current county by calculated number of all communities in it.
            county_dict["Communities"] += len(any_type_of_community_in_county)

        # NOTE: Get the dictionary with the largest amount of the "Communities" in it from the "list_of_all_counties_dict".
        the_largest_county = max(list_of_all_counties_dict, key=operator.itemgetter("Communities"))

        # NOTE: Return only the specific values of the largest county: its "Name" and number of "Communities".
        final_county_data = []
        final_county_data.extend([("powiat {}".format(the_largest_county.get("Name")), the_largest_county.get("Communities"))])

        return final_county_data
