import urllib.request
import json

sourceJsonURL = 'https://api.nhk.or.jp/nhkworld/epg/v6/world/all.json?apikey=EJfK8jdS57GqlupFgAfAAwr573q01y6k'
with urllib.request.urlopen(sourceJsonURL) as url:
    data = json.load(url)
    with open('downloadedjson.json', 'w') as jsonfile:
        print(data, file=jsonfile)
