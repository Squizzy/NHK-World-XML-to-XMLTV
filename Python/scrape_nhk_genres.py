""" Python (python 3 only) application to fetch the EPG genres that NHK uses"""

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


# Download the content of pages baseNHKGrensURL/<number> 
# where <number> is the genre. 
# If there is a genre, there is a page, it seems.
# and extract the genre from the title (Thank you NHK!). 
# Update the genres dictionary if a page existed
# Saves the list of a file


# Location of where the NHK categories could be found (at the time of the creation of this file)
BASE_URL_FOR_NHK_GENRES = "https://www3.nhk.or.jp/nhkworld/en/shows/category/"

SAVED_GENRES_FILE = "genres.txt"

# Type hint then initiate genres with the None value (used when no genre is provided)
genres: dict[int|None, str]

genres = {
    None: "General"
    }


def parse_html(url) -> BeautifulSoup|None:
    """ Fetches content from a URL and parses it with BeautifulSoup.
    
    Args:
        url (str): the URL to try and fetch from the internet

    Returns:
        str|None: the html of the requested page, if it exists, otherwise None
    """
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        # print(f"Failed to retrieve the webpage: status code {response.status_code}")
        print("Not assigned by NHK")
        return None


def indentify_and_acquire_genre(genre) -> str|None:
    """ For a given genre number, try to retrieve the assigned string value

    Args:
        genre (int): integer that may have a genre assigned to, by NHK

    Returns:
        str|None: the genre, in english, of the corresponding genre number, otherwise None
    """
    # for genre in range(100):
    # print the number with leading space(s) if less that 3 digits
    print(f"{genre: >3d}: ", end="")
    
    soup = parse_html(BASE_URL_FOR_NHK_GENRES + str(genre))
    
    if soup:
        # print(soup)
        title = soup.title.text # type: ignore
        
        value = (re.findall('Watch (.*) Videos', title))[0]
        print(value)
        return value
    else:
        # print("Not assigned.")
        return None


def save_genres() -> None:
    """ Saves the list of genres to a file.
    Currently no error checking is performed
    """
    # Save the formatted version of the dictionar into a file, 
    # ready to be copy/pasted into the NHK XMLTV generator app
        # f.write("genres = " + str(genres).replace(", ", ",\n          ").replace("}", "\n}"))            

    with open(SAVED_GENRES_FILE, 'w') as f:
        f.write("genres = {\n")
        for key in genres:
            f.write(f'\t{str(key)}: "{str(genres[key])}"\n')
        f.write("}")


def get_genres(min:int = 0, max:int = 100) -> dict[int|None, str]:
    """retrives all the genres in the min-max range given and return a dictionary of the ones found

    Args:
        min (int, optional): lowest genre number, included. Defaults to 0.
        max (int, optional): highest genre number, not included. Defaults to 100.

    Returns:
        dict[int|None, str]: a dictionary with the list of genres found in the range given
    """
    scanned_genres: dict[int|None, str] = {None: "General"}
    
    for genre in range(min, max):
        g = indentify_and_acquire_genre(genre)
        if g:
            scanned_genres[genre] = g
            
    return scanned_genres


def main() -> int:
    # Try for genre 0 to 99 
    # Though currently only 11 to 31 seem to be used
    
    global genres
    genres = get_genres(min=8, max=32)

    save_genres()
        
    return 0


if  __name__ in "__main__":
    main()