import operator


class Voivodeship:
    """
    Parent class using for creating instances
    of the current locations in a voivodeship
    (e.g. cities, towns, villages, delegatures).
    """
    def __init__(self, voivodeship_id, county_id, community_id, community_type_id, region_name, region_type_name):
        self.voivodeship = voivodeship_id
        self.county = county_id
        self.community = community_id
        self.community_type = community_type_id
        self.name = region_name
        self.type = region_type_name


class LocationList:
    """
    Independent class using for aggregating the instances
    of the class "Voivodeship" and for operating on them.
    """
    list_of_locations = []

    def add_location(self, current_location):
        """
        Method for append to the class attribute "list_of_locations" instances of the "Voivodeship" class.
        """
        self.list_of_locations.append(current_location)

    def voivodeship_name(self):
        """
        Method for finding the name of a current voivodeship in the CSV file.

        Returns:
            string
        """
        name_of_the_voivodeship = None

        for location in self.list_of_locations:
            # Insensitiveness for uppercase letters.
            type_of_location = location.type.lower()
            # Take into consideration only the following location type: "Voivodeship".
            if type_of_location == "województwo":
                name_of_the_voivodeship = location.name

        return name_of_the_voivodeship

    def list_statistics(self):
        """
        Method to count the occurrences of the specific types of locations from
        the indicated CSV file and to convert the gained data to the list of tuples.

        Returns:
            list of tuples with strings
        """
        # Calculate the following statistics.
        number_of_different_counties = set()
        number_of_urban_municipalities = 0
        number_of_rural_municipalities = 0
        number_of_urban_rural_municipalities = 0
        number_of_villages = 0
        number_of_towns = 0
        number_of_cities = 0

        for location in self.list_of_locations:
            # Count the unique occurrences of the different "Counties".
            if location.county != "":
                number_of_different_counties.add(location.county)
                different_counties_name = "powiaty"

            # Count the occurrences of the following location type: "Urban municipality".
            if location.community_type == "1":
                number_of_urban_municipalities += 1
                urban_municipalities_name = location.type

            # Count the occurrences of the following location type: "Rural municipality".
            if location.community_type == "2":
                number_of_rural_municipalities += 1
                rural_municipalities_name = location.type

            # Count the occurrences of the following location type: "Urban-rural municipality".
            if location.community_type == "3":
                number_of_urban_rural_municipalities += 1
                urban_rural_municipalities_name = location.type

            # Count the occurrences of the following location type: "Village".
            if location.community_type == "5":
                number_of_villages += 1
                villages_name = location.type

            # Count the occurrences of the following location type: "Town".
            if location.community_type == "4":
                number_of_towns += 1
                towns_name = location.type

            # Insensitiveness for uppercase letters.
            type_of_location = location.type.lower()
            # Count the occurrences of the following location type: "City".
            if type_of_location == "miasto na prawach powiatu":
                number_of_cities += 1
                cities_name = location.type

        # Create the dictionaries from the "location.type" (name of location type) as the KEY, and count of occurrences as the VALUE.
        dict_different_counties = {different_counties_name: len(number_of_different_counties)}
        dict_urban_municipalities = {urban_municipalities_name: number_of_urban_municipalities}
        dict_rural_municipalities = {rural_municipalities_name: number_of_rural_municipalities}
        dict_urban_rural_municipalities = {urban_rural_municipalities_name: number_of_urban_rural_municipalities}
        dict_villages = {villages_name: number_of_villages}
        dict_towns = {towns_name: number_of_towns}
        dict_cities = {cities_name: number_of_cities}

        # Stack the dictionaries all together in a tuple.
        tuple_of_all_dictionaries = (dict_different_counties, dict_urban_municipalities, dict_rural_municipalities,
                                    dict_urban_rural_municipalities, dict_villages, dict_towns, dict_cities)

        # Save the values and keys from all dictionaries in the dedicated list.
        all_dictionaries_items = []

        for one_dictionary in tuple_of_all_dictionaries:
            for key, value in one_dictionary.items():
                all_dictionaries_items.extend([(str(value), key)])  # Add collection of string-type items as tuple to the list of tuples.

        return all_dictionaries_items

    def longest_names(self):
        """
        Method to count the name length of all locations from
        the database and get the longest name (by default: top 3).

        Returns:
            list of lists with strings
        """
        # List of all dictionaries generated below.
        all_location_name_dictionaries = []

        for location in self.list_of_locations:
            # Take into consideration only the following location type: "City".
            if location.community_type == "4":
                name_length = len(location.name)
                name = location.name
                # Make a dictionaries from the "name" and "name_length" of the current location as the KEY and VALUE, respectively.
                dict_location_name = {"Name": name, "Name length": name_length}
                all_location_name_dictionaries.append(dict_location_name)

        # Sort the gained dictionaries in descending order by their keys ("Name length").
        sorted_list = sorted(all_location_name_dictionaries, key=operator.itemgetter("Name length"), reverse=True)

        # Get the first three longest names from the list.
        the_longest_name = []

        for number, location in enumerate(sorted_list):
            if number < 3:
                the_longest_name.append([location.get("Name")])

        return the_longest_name
