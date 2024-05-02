""" Python application to convert NHK EPG in JSON into XMLTV standard"""
__author__ = "Squizzy"
__copyright__ = "Copyright 2019, Squizzy"
__credits__ = "The respective websites, and whoever took time to share information\
                 on how to use Python and modules"
__license__ = "GPL"
## Refactoring
__version__ = "1.2"
__maintainer__ = "Squizzy"

import json
from datetime import datetime, timezone
import xml.etree.ElementTree as xml
import urllib.request

DEBUG = False

# jsonInFile = 'all-json-example.json'
jsonInFile = 'DownloadedJSON.json'
# reference for later when pulling off the internet directly:
#fxbx 7-20-2023 new authentication-less URL? replacing:
JsonInURL = "https://nwapi.nhk.jp/nhkworld/epg/v7b/world/all.json"
XMLOutFile = 'ConvertedNHK.xml'

rootURL = "https://www3.nhk.or.jp"
ChannelIconURL = rootURL + "nhkworld/assets/images/icon_nhkworld_tv.png"

# In case the time offset is incorrect in the XMLTV file, the value below 
# can be modified to adjust it: For example -0100 would change to -1 UTC
timeOffset = ' +0000'

# Import the .json from the URL
with urllib.request.urlopen(JsonInURL) as url:
    data = json.load(url)
if DEBUG:
    with open(jsonInFile, 'w', encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile)


## Replaced deprecated utcfromtimestamp() method
# def adj_date(u): return datetime.utcfromtimestamp(int(u[:-3])).strftime('%Y%m%d%H%M%S')
def convert_unix_to_xmltv_date(u):
    """ Converts the unit time from NHK to XMLTV time format

    Args:
        u (str): Unix time in milliseconds as a string

    Returns:
        str: Returns the date in XMLTV format required for applications like Kodi.
    """    
    return datetime.fromtimestamp(int(u[:-3]), tz = timezone.utc).strftime('%Y%m%d%H%M%S')

def add_xml_element(parent, tag, attributes=None, text=None):
    """ Add an XML element to a tree

    Args:
        parent (xml.Element): The parent node in the XML tree
        tag (str): The name of the XML tag to be added.
        attributes (dict, optional): Dictionary of attributes for the XML tag. Defaults to None.
        text (str, optional): The text content for the XML element. Defaults to None.

    Returns:
        xml.Element: the XML node created
    """
    element = xml.SubElement(parent, tag)
    if attributes:
        for key, value in attributes.items():
            element.set(key, value)
    if text:
        element.text = text
    return element

def indent(elem, level=0):
    """ indent: beautify the xml to be output, rather than having it stay on one line
        Origin: http://effbot.org/zone/element-lib.htm#prettyprint """
    i = "\n" + level * "\t"
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "\t"
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


# genres values come from NHK network under "genre" to become "category" in xmltv
genres = {None: "General",
          11: "News",
          12: "Current Affairs",
          13: "International (13 - to be confirmed)",
          14: "Biz/Tech",
          15: "Documentary",
          16: "Interview",
          17: "Food",
          18: "Travel",
          19: "Art & Design",
          20: "Culture & Lifestyle",
          21: "Entertainment",
          22: "Pop Culture & Fashion",
          23: "Science & Nature",
          24: "Documentary",
          25: "Sports",
          26: "Drama",
          27: "Interactive",
          28: "Learn Japanese",
          29: "Disaster Preparedness",
          30: "Kids", #fxbx: last cat as of 7-20-2023
          31: "Anime Manga (31 - to be confirmed)"
}

# Start filling in the table XML tree with content that is useless and might not change
root = xml.Element('tv')
root.set('source-data-url', JsonInURL)
root.set('source-info-name', 'NHK World EPG Json')
root.set('source-info-url', 'https://www3.nhk.or.jp/nhkworld/')

channel = add_xml_element(root, 'channel', attributes={'id': 'nhk.world'})
add_xml_element(channel, 'display-name', text='NHK World')
add_xml_element(channel, 'icon', attributes={'src': ChannelIconURL})
#add_xml_element(root, 'channel1', attributes={'id': 'nhk.world'})
# channel = xml.SubElement(root, 'channel')
# channel.set('id', 'nhk.world')
#channelDisplayName = add_xml_element(channel, 'display-name', text='NHK World')
# channelDisplayName = xml.SubElement(channel, 'display-name')
# channelDisplayName.text = 'NHK World'
#channelIcon = add_xml_element(channel, 'icon', attributes={'src': ChannelIconURL})
# channelIcon = xml.SubElement(channel, 'icon')
# channelIcon.set('src', ChannelIconURL)

if DEBUG:
    # load the json file from local storage
    with open(jsonInFile, 'r', encoding='utf8') as nhkjson:
        nhkimported = json.load(nhkjson)
else:
    nhkimported = data

# Go through all items, though only interested in the Programmes information here
for item in nhkimported["channel"]["item"]:

    # construct the program info xml tree
    programme = add_xml_element(root, 'programme', attributes={'start': convert_unix_to_xmltv_date(item["pubDate"]) + timeOffset, 
                                                               'stop': convert_unix_to_xmltv_date(item["endDate"]) + timeOffset, 
                                                               'channel':'nhk.world'})
    # programme1 = xml.SubElement(root, 'programme1')
    # programme1.set('start', convert_unix_to_xmltv_date(item["pubDate"]) + timeOffset)
    # programme1.set('stop', convert_unix_to_xmltv_date(item["endDate"]) + timeOffset)
    # programme1.set('channel', 'nhk.world')

    progTitle = add_xml_element(programme, 'title', attributes={'lang': 'en'}, text=item["title"])
    # progTitle1 = xml.SubElement(programme1, 'title')
    # progTitle1.set('lang', 'en')
    # progTitle1.text = item["title"]

    progTitle = add_xml_element(programme, 'sub-title', attributes={'lang': 'en'}, text=item["subtitle"])
    # progSub = xml.SubElement(programme, 'sub-title')
    # progSub.set('lang', 'en')
    # progSub.text = item["subtitle"]

    progTitle = add_xml_element(programme, 'desc', attributes={'lang': 'en'}, text=item["description"])
    # progDesc = xml.SubElement(programme, 'desc')
    # progDesc.set('lang', 'en')
    # progDesc.text = item["description"]

    genre = item["genre"]["TV"]
    category2 = ""
    if genre == "":
        category1 = genres[None]
    elif isinstance(genre, str):
        category1 = genres[int(genre)].lower()
    elif isinstance(genre, list):
        category1 = genres[int(genre[0])].lower()
        category2 = genres[int(genre[1])].lower()
    else:
        category1 = genres[None]

    progCat1 = add_xml_element(programme, 'category', attributes={'lang': 'en'}, text=category1)
    # progCat1 = xml.SubElement(programme, 'category')
    # progCat1.set('lang', 'en')
    # progCat1.text = category1

    if category2 != "":
        progCat2 = add_xml_element(programme, 'category', attributes={'lang': 'en'}, text=category2)
        # progCat2 = xml.SubElement(programme, 'category')
        # progCat2.set('lang', 'en')
        # progCat2.text = category2

    progEpNum = add_xml_element(programme, 'episode-num', text=item["airingId"])
    # progEpNum = xml.SubElement(programme, 'episode-num')
    # progEpNum.text = item["airingId"]

    progEpNum = add_xml_element(programme, 'icon', attributes={'src': rootURL + item["thumbnail"]})
    # progIcon = xml.SubElement(programme, 'icon')
    # progIcon.set('src', rootURL + item["thumbnail"])

indent(root)

# Export the xml to a local file
tree = xml.ElementTree(root)
with open(XMLOutFile, 'w+b') as outFile:
    tree.write(outFile)
