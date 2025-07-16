""" Python (python 3 only) application to fetch the EPG genres that NHK uses"""

__author__ = "Squizzy"
__copyright__ = "Copyright 2019-now, Squizzy"
__credits__ = "The respective websites, and whoever took time to share information\
                 on how to use Python and modules"
__license__ = "GPLv2"
## updated version following changes proposed by fxbx below
__version__ = "1.3"
__maintainer__ = "Squizzy"


import requests
import re
import sys
from bs4 import BeautifulSoup # type: ignore


# Downloads the content of pages BASE_URL_FOR_NHK_GENRES/<categoryNumber> 
# If the categoryNumber is assigned a genre, a page exists at the above URL, containing a HTML page.
# The genre is the title in this HTML (Thank you NHK!). 
# Update the genres dictionary if a page existed
# Saves the list of a file


# Location of where the NHK categories could be found (at the time of the creation of this file)
# Genres are in a HTML at location https://www3.nhk.or.jp/nhkworld/en/shows/category/<categoryNumber>
# where <categoryNumber> is the number of the genre, from 0 to 99.
# NHK site responds with 403 if the categoryNumber has not been assigned to a genre
BASE_URL_FOR_NHK_GENRES = "https://www3.nhk.or.jp/nhkworld/en/shows/category/"

SAVED_GENRES_FILE = "genres.txt"


def probe_nhk_category_number(categoryNumber) -> BeautifulSoup|None:
    """ Fetches content from a URL and parses it with BeautifulSoup.
    
    Args:
        url (str): the URL to try and fetch from the internet

    Returns:
        str|None: the html of the requested page, if it exists, otherwise None
    """
    url = BASE_URL_FOR_NHK_GENRES + str(categoryNumber)
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    
    elif response.status_code == 404:
        print(f"Network error {response.status_code}: {url} The NHK file containing the genres does not exist at the URL provided")
        sys.exit(1)
        
    elif response.status_code == 403:
        # print(f"Network error {response.status_code} for category: {categoryNumber}")
        # Response received if NHK has not attached a genre to the categoryNumber
        return None
    
    else:
        print(f"Network error {response.status_code}: Problem with the URL to the NHK JSON file provided")
        sys.exit(1)



def retrieve_genre_from_category(categoryNumber: int) -> str|None:
    """ For a given categoryNumber, if the NHK has assigned a genr, extract the genre name.
    The genre is the title of the page returned by the NHK server.
    if an error 403 was return, no answer was received so no genre was assigned

    Args:
        categoryNumber (int): NHK category number tested that NHK might have assigned a genre to

    Returns:
        str|None: the genre, in english, of the categoryNumber if it exists, otherwise None
    """

    # print the number with leading space(s) if less that 3 digits
    print(f"{categoryNumber: >3d}: ", end="")
    
    soup = probe_nhk_category_number(categoryNumber)
    
    if soup:
        title: str = soup.title.text # type: ignore
        
        # find the text between "Watch " and " Videos" in the <title> tag of the HTML recovered
        value = (re.findall('Watch (.*) Videos', title))[0]
        print(value)
        return value
    else:
        print("Not assigned.")
        return None


def get_genres(min:int = 0, max:int = 100) -> dict[int|None, str]:
    """Collect the genres existing for the min-max categoryNumber range into a dictionary

    Args:
        min (int, optional): lowest category number, included. Defaults to 0.
        max (int, optional): highest category number, not included. Defaults to 100.

    Returns:
        dict[int|None, str]: a dictionary with the list of genres found in the range given
                key: (int) category number (only if genre associated), or None for general
                value: (str) the genre name, in english, or "General" for None
    """
    
    genres: dict[int|None, str] = {None: "General"}
    genres = { None: "General" }
    
    for categoryNumber in range(min, max):
        genre: str | None = retrieve_genre_from_category(categoryNumber)
        
        # if a genre is found, record it
        if genre is not None:
            genres.update({categoryNumber: genre})
            
    return genres


def save_genres(genres: dict[int|None, str]) -> None:
    """ Saves the list of genres to a file.

    Args:
        genres (dict[int|None, str]): the dictionary of genres to save
    """
    # Save the formatted version of the dictionary into a file, 
    # ready to be copy/pasted into the NHK XMLTV generator app

    firstLine: str = "GENRES: dict[int|None, str] = {\n"

    fileContent: str = firstLine
    
    for categoryNumber in genres:
        fileContent += f'\t{str(categoryNumber)}: "{str(genres[categoryNumber])}"\n'

    fileContent += "}"
    
    try:
        with open(SAVED_GENRES_FILE, 'w') as f:
            f.write(fileContent)
                
    except IOError as e:
        print(f"Error writing to file {SAVED_GENRES_FILE}: {e}")
        sys.exit(1)
        
    else:
        print(f"{SAVED_GENRES_FILE} saved successfully")
        

def main() -> int:
    # Try for genre 8 to 40 
    # Though currently only 11 to 31 seem to be used
    
    genres: dict[int|None, str] = get_genres(min=8, max=40)

    save_genres(genres)
        
    return 0


if  __name__ in "__main__":
    main()