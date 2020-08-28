from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import re

# All found items
total_items_found = 0
ministries = []


class Ministry:
    def __init__(self, name):
        self.name = name

        # Empty list for all subordinate units
        self.subordinate_units = []
        self.num_items_found = 0

    def __str__(self):
        return '{} has {} subordinate units.'.format(self.name, len(self.subordinate_units))


class SubordinateUnit(Ministry):
    def __init__(self, name, site_link):
        # Link that redirects to homepage of SubordinateUnit
        self.site_link = site_link
        self.name = name
        self.ministry_name = Ministry.__init__(self, name)

    def __str__(self):
        return '{} is subordinate unit of {}. Link: {}'.format(self.name, self.ministry_name, self.site_link)


# Initialization of Selenium Worker
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.gov.pl/web/gov/ministerstwa")

# Looking for all Ministries names
for i in driver.find_elements_by_xpath('//section/ul/li/h3/a'):
    ministries.append(Ministry(i.text))

# Iterating over groups of subordinate units
# for group in driver.find_elements_by_xpath('//section/section/ul/li/ul'):
#     # Looking for all SubordinateUnits links and names
#     for group 

group = driver.find_elements_by_xpath('//section/section/ul/li/ul')
# Showing random Ministry results


# Closing web driver
driver.close()
