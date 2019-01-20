__author__ = "Squizzy"
__copyright__ = "Copyright 2019, Squizzy"
__credits__ = "The respective websites, and whoever took time to share information on how to use Python and modules"
__license__ = "GPL"
__version__ = "1.0.3"
__maintainer__ = "Squizzy"

import json
import datetime
import xml.etree.ElementTree as xml

jsonInFile = 'all-json-example.json'
# reference for later when pulling off the internet directly:
# JsonInURL = 'https://api.nhk.or.jp/nhkworld/epg/v6/world/all.json?apikey=EJfK8jdS57GqlupFgAfAAwr573q01y6k'
XMLOutFile = 'ConvertedNHK.xml'


# adj_date: convert the unix date with extra 3 "0" to the xmltv date format
def adj_date(u): return datetime.datetime.utcfromtimestamp(int(u[:-3])).strftime('%Y%m%d%H%M%S')


# indent: beautify the xml to be output, rather than having it stay on one line
# Origin: http://effbot.org/zone/element-lib.htm#prettyprint
def indent(elem, level=0):
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
          25: "Sports"}

# Start filling in the table XML tree with content that is useless and might not change
root = xml.Element('tv')
root.set('source-data-url', 'https://api.nhk.or.jp/nhkworld/epg/v6/world/all.json?apikey=\
EJfK8jdS57GqlupFgAfAAwr573q01y6k')
root.set('source-info-name', 'NHK World EPG Json')
root.set('source-info-url', 'https://www3.nhk.or.jp/nhkworld/')

channel = xml.SubElement(root, 'channel')
channel.set('id', 'nhk.world')
channelDisplayName = xml.SubElement(channel, 'display-name')
channelDisplayName.text = 'NHK World'
channelIcon = xml.SubElement(channel, 'icon')
channelIcon.set('src', 'https://www3.nhk.or.jp/nhkworld/assets/images/icon_nhkworld_tv.png')

# load the json file from local storage
with open(jsonInFile, 'r', encoding='utf8') as nhkjson:
    nhkimported = json.load(nhkjson)

# Go through all items, though only interested in the Programmes information here
for item in nhkimported["channel"]["item"]:

    # The useful information, ready to be inserted
    start = adj_date(item["pubDate"])
    end = adj_date(item["endDate"])
    title = item["title"]
    subtitle = item["subtitle"]
    description = item["description"]
    episodeNum = item["airingId"]
    iconLink = "https://www3.nhk.or.jp" + item["thumbnail"]
    genre = item["genre"]["TV"]
    if genre == "":
        category = genres[None]
    elif isinstance(genre, str):
        category = genres[int(genre)]
    elif isinstance(genre, list):
        category = genres[int(genre[0])]
    else:
        category = genres[None]

    # construct the program info xml tree
    programme = xml.SubElement(root, 'programme')
    programme.set('start', start + ' +0000')
    programme.set('stop', end + ' +0000')
    programme.set('channel', 'nhk.world')
    progTitle = xml.SubElement(programme, 'title')
    progTitle.set('lang', 'en')
    progTitle.text = title
    progSub = xml.SubElement(programme, 'sub-title')
    progSub.set('lang', 'en')
    progSub.text = subtitle
    progDesc = xml.SubElement(programme, 'desc')
    progDesc.set('lang', 'en')
    progDesc.text = description
    progCat1 = xml.SubElement(programme, 'category')
    progCat1.set('lang', 'en')
    progCat1.text = category
    progEpNum = xml.SubElement(programme, 'episode-num')
    progEpNum.text = episodeNum
    progIcon = xml.SubElement(programme, 'icon')
    progIcon.set('src', iconLink)

indent(root)

# Export the xml to a local file
tree = xml.ElementTree(root)
with open(XMLOutFile, 'w+b') as outFile:
    tree.write(outFile)
