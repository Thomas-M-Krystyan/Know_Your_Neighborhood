import data_manager
from main import *


class Voivodeship:

    def __init__(self, voivodeship_id, county_id, community_id, community_type_id, region_name, region_type_name):
        """
        Create instances of current locations in the voivodeship (cities, towns, villages, districts).
        """
        self.voivodeship = voivodeship_id  # All cities, towns and villages are in "Małopolskie" voicodeship by default.
        self.county = county_id
        self.community = community_id
        self.community_type = community_type_id
        self.name = region_name
        self.type = region_type_name


class County(Voivodeship):

    def __init__(self):
        pass


class Community(Voivodeship):

    def __init__(self):
        pass


class CommunityType(Voivodeship):

    def __init__(self):
        pass


class LocationList:

    list_of_locations = []

    def __init__(self):
        """
        """

    def add_location(self, current_location):
        """
        """
        self.list_of_locations.append(current_location)

    def list_statistics(self):
        """
        Method used to count the occurrences of the specific types of locations
        from the indicated CSV file and convert the data to the list of tuples.

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

        for element in self.list_of_locations:
            # Count the unique occurrences of the different "Counties".
            if element.county != "":
                number_of_different_counties.add(element.county)
                different_counties_name = "powiaty"
            # Count the occurrences of the location type: "Urban municipality".
            if element.community_type == "1":
                number_of_urban_municipalities += 1
                urban_municipalities_name = element.type
            # Count the occurrences of the location type: "Rural municipality".
            if element.community_type == "2":
                number_of_rural_municipalities += 1
                rural_municipalities_name = element.type
            # Count the occurrences of the location type: "Urban-rural municipality".
            if element.community_type == "3":
                number_of_urban_rural_municipalities += 1
                urban_rural_municipalities_name = element.type
            # Count the occurrences of the location type: "Village".
            if element.community_type == "5":
                number_of_villages += 1
                villages_name = element.type
            # Count the occurrences of the location type: "Town".
            if element.community_type == "4":
                number_of_towns += 1
                towns_name = element.type
            # Count the occurrences of the location type: "City".
            if element.type == "miasto na prawach powiatu":
                number_of_cities += 1
                cities_name = element.type

        # Create the dictionaries from "element.type" (name of location type) as the KEY, and count of occurrences as the VALUE.
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
                all_dictionaries_items.extend([(str(value), key)])  # Add pair of an items as tuple to the list of tuples.

        return all_dictionaries_items
