# Conversion of NHK's EPG in JSON to XMLTV - v1.2

## CreateNHKXMLTV.py
Python v3 (under Python folder above)
* Only file `CreateNHKXMLTV.py` is needed (+ Python on the machine on which it is run of course).
* Requires Python 3.x.
* Runs on Windows, MacOS, Linux.

Python v2
* --> branch p2 implements using python v2 as per dazzhk implementation. it is not merged into master yet as it is not tested.
* Requires Python 2.x.
* Should run on Windows, MacOS, Linux.
* Any feedback on testing welcome.

## scrape_nhk_genres.py
NEW: NHK genres scraper
* goes through the NHK website and attempts to extract genres as NHK defines them.
* Saves the result into a text file, `genres.txt`.
* The content of this text file can be copied and pasted into the create `CreateNHKXMLTV.py` file before it is run so the latest genres can be applied.
* Requires Python 3.x.
* Runs on Windows, MacOS, Linux.


## Note:
All other files in this repository have no value and are only here for historical reason (until they are removed)