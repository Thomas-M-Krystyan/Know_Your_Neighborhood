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
        """
        different_counties = set()
        urban_municipalities = 0
        rural_municipalities = 0
        urban_rural_municipalities = 0
        villages = 0
        towns = 0
        cities = 0

        for element in self.list_of_locations:
            # Count the unique occurrences of the different "Counties".
            if element.county != "":
                different_counties.add(element.county)
                different_counties_name = "powiaty"
            # Count the occurrences of the community type: "Urban municipality".
            if element.community_type == "1":
                urban_municipalities += 1
                urban_municipalities_name = element.type
            # Count the occurrences of the community type: "Rural municipality".
            if element.community_type == "2":
                rural_municipalities += 1
                rural_municipalities_name = element.type
            # Count the occurrences of the community type: "Urban-rural municipality".
            if element.community_type == "3":
                urban_rural_municipalities += 1
                urban_rural_municipalities_name = element.type
            # Count the occurrences of the community type: "Village".
            if element.community_type == "5":
                villages += 1
                villages_name = element.type
            # Count the occurrences of the community type: "Town".
            if element.community_type == "4":
                towns += 1
                towns_name = element.type
            # Count the occurrences of the community type: "City".
            if element.type == "miasto na prawach powiatu":
                cities += 1
                cities_name = element.type

        dict_different_counties = {"powiaty": len(different_counties)}
        for key, value in dict_different_counties.items():
            print(value, key)

        dict_urban_municipalities = {urban_municipalities_name: urban_municipalities}
        for key, value in dict_urban_municipalities.items():
            print(value, key)

        dict_rural_municipalities = {rural_municipalities_name: rural_municipalities}
        for key, value in dict_rural_municipalities.items():
            print(value, key)

        dict_urban_rural_municipalities = {urban_rural_municipalities_name: urban_rural_municipalities}
        for key, value in dict_urban_rural_municipalities.items():
            print(value, key)

        dict_villages = {villages_name: villages}
        for key, value in dict_villages.items():
            print(value, key)

        dict_towns = {towns_name: towns}
        for key, value in dict_towns.items():
            print(value, key)

        dict_cities = {cities_name: cities}
        for key, value in dict_cities.items():
            print(value, key)
