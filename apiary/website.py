"""
Base class for WikiApiary websites.
"""
# pylint: disable=C0301

# Import the task classes associated with websites
from WikiApiary.apiary.tasks.website.extensions import RecordExtensionsTask
from WikiApiary.apiary.tasks.website.general import RecordGeneralTask
from WikiApiary.apiary.tasks.website.maxmind import MaxmindTask
from WikiApiary.apiary.tasks.website.skins import RecordSkinsTask
from WikiApiary.apiary.tasks.website.whois import RecordWhoisTask
from WikiApiary.apiary.tasks.website.statistics import GetStatisticsTask


class Website(object):
    """Class for websites in WikiApiary."""

    def __init__(self, website_id, website_name, api_url):
        """Initialize the instance."""
        self.__has_id = website_id
        self.__website_name = website_name
        self.__has_api_url = api_url

    def record_general(self):
        """Get extension data."""
        RecordGeneralTask.delay(self.__has_id, self.__website_name, self.__has_api_url)

    def record_extensions(self):
        """Get extension data."""
        RecordExtensionsTask.delay(self.__has_id, self.__website_name, self.__has_api_url)

    def record_skins(self):
        """Get extension data."""
        RecordSkinsTask.delay(self.__has_id, self.__website_name, self.__has_api_url)

    def record_maxmind(self):
        """Get extension data."""
        MaxmindTask.delay(self.__has_id, self.__website_name, self.__has_api_url)

    def record_whois(self):
        """Get whois data."""
        RecordWhoisTask.delay(self.__has_id, self.__website_name, self.__has_api_url)

    # def record_smwinfo(self):
    #     """Get extension data."""
    #     tasks.record_smwinfo.delay(self.__has_id, self.__website_name, self.__has_api_url)

    def get_statistics(self):
        """Run the statistics task"""
        GetStatisticsTask.delay(self.__has_id, self.__website_name, self.__has_api_url)

