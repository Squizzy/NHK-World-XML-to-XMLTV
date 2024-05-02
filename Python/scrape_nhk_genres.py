import requests, re
from bs4 import BeautifulSoup

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



baseNHKGenresURL = "https://www3.nhk.or.jp/nhkworld/en/shows/category/"

genre = "19"

urlToProbe = baseNHKGenresURL + genre

genres=[]

with open('genres.txt', 'w') as f:
    for genre in range(100):
        print(genre)
        soup = parse_html(baseNHKGenresURL + str(genre))
        if soup:
            title = soup.find('title').text
            value =  str((re.findall('Watch (.*) Videos', title)))
            value = value[2:][:len(value)-4]
            # genres.append({genre: value})
            f.write("          " + str(genre) + f': "{value}",\n')        
    
# print (genres)


    # print("Title of the page:", title)
    # print("Title of the page:", re.findall('Watch (.*) Videos', title))
    # Find all 'a' tags
    # links = soup.find_all('a')
    # for link in links:
    #     print(link.get('href'))