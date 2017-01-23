from data_manager import *


class Voivodeship:

    def __init__(self, voivodeship_id, county_id, community_id, community_type_id, region_name, region_type_name):
        """
        Create instances of current locations in the voivodeship (cities, towns, villages, districts).
        """
        self.voivodeship = voivodeship_id  # All cities, towns and villages are in "Małopolskie" voicodeship by default.
        self.county = county_id
        self.community = community_id
        self.community_type = community_type_id
        self.region_name = region_name
        self.region_type_name = region_type_name

    def list_statistics(self):
        # header = ("MAŁOPOLSKIE", "")

        # original_file_content = data_manager.csv_reader("malopolska.csv")
        # converted_file_content = data_manager.table_converter(original_file_content)

        # for elements in converted_file_content.county:
        #     print(elements)
        pass


class County(Voivodeship):

    def __init__(self):
        pass


class Community(Voivodeship):

    def __init__(self):
        pass


class CommunityType(Voivodeship):

    def __init__(self):
        pass
