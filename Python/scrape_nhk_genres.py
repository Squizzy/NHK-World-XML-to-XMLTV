""" Python application to convert NHK EPG in JSON into XMLTV standard"""
__author__ = "Squizzy"
__copyright__ = "Copyright 2019-now, Squizzy"
__credits__ = "The respective websites, and whoever took time to share information\
                 on how to use Python and modules"
__license__ = "GPL"
## updated version following changes proposed by fxbx below
__version__ = "1.0"
__maintainer__ = "Squizzy"


import requests
import re
from bs4 import BeautifulSoup



# Location of where the NHK categories could be found (at the time of the creation of this file)
baseNHKGenresURL = "https://www3.nhk.or.jp/nhkworld/en/shows/category/"

# Type hint then initiate genres with the None value (used when no genre is provided)
genres: dict[int|None, str]

genres = {
    None: "General"
    }


def parse_html(url):
    """Fetches content from a URL and parses it with BeautifulSoup."""
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        print(f"Failed to retrieve the webpage: status code {response.status_code}")
        return None


# Download the content of pages baseNHKGrensURL/<number> 
# where <number> is the genre. 
# If there is a genre, there is a page, it seems.
# and extract the genre from the title (Thank you NHK!). 
# Update the genres dictionary if a page existed

for genre in range(100):
    print(genre)
    soup = parse_html(baseNHKGenresURL + str(genre))
    if soup:
        title = soup.find('title').text
        value =  str((re.findall('Watch (.*) Videos', title)))
        value = value[2:][:len(value)-4]
        genres[int(genre)]= value

# Save the formatted version of the dictionar into a file, 
# ready to be copy/pasted into the NHK XMLTV generator app
with open('genres.txt', 'w') as f:
    f.write("genres = " + str(genres).replace(", ", ",\n          ").replace("}", "\n}"))
