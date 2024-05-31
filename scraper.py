import requests
from bs4 import BeautifulSoup


req = requests.get('https://www.bankofalbania.org/Tregjet/Kursi_zyrtar_i_kembimit/')

soup = BeautifulSoup(req.text, 'lxml')
eu = ''
us = ''

table = soup.find_all('table')[0]
trs = table.find_all('tr')
for tr in trs:
    try:
        if tr.find_all('td')[0].text == 'Dollar Amerikan':
            us = tr.find_all('td')[2].get_text()
        if tr.find_all('td')[0].text == 'Euro':
            eu = tr.find_all('td')[2].get_text()
    except:
        pass

import os
import re, math


def edit_settings_variable(variable_name, new_value):
    # Path to settings.py file
    settings_file = r'C:\Users\User\store_manager\store_manager\settings.py'

    # Regular expression pattern to match the variable assignment
    pattern = re.compile(r'^(?P<variable>{})\s*=\s*(?P<value>.*)'.format(re.escape(variable_name)), re.MULTILINE)

    # Read the content of settings.py
    with open(settings_file, 'r') as file:
        content = file.read()

    # Search for the variable assignment in the content
    match = pattern.search(content)

    if match:
        # Replace the old value with the new value
        new_content = pattern.sub(r'\g<variable> = {}'.format(repr(new_value)), content)

        # Write the modified content back to settings.py
        with open(settings_file, 'w') as file:
            file.write(new_content)

        print(f"Variable '{variable_name}' in settings.py has been updated to '{new_value}'.")
    else:
        print(f"Variable '{variable_name}' not found in settings.py.")


# Example usage:
edit_settings_variable('EURO', math.ceil(float(eu)))
edit_settings_variable('DOLLAR', math.ceil(float(us)))
