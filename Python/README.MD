# Requirements:
 - Python 3.x (tested with Python 3.7)
 - NO LONGER USED WITH V1.1: The correct json file stored in the same folder, called "all-json-example.json"

# To run the program:
- From Windows command line: "python.exe .\CreateNHKXMLTV.py"
- From Mac "python ./CreateNHKXMLTV.py" or "python-3.7 ./CreateNHKXMLTV.py" if needed
- Linux - not tested yet, but should be same as Mac

# Versions
15 Apr 2024 - v1.2 - updated URL as per fxbx update, replaced deprecated utcfromtimestamp(), cleaned up XML tree generation, added some new genres, added timeOffsetVariable

21 Jan 2019 - V1.1 - Windows Executable created using "auto-py-to-exe.exe .\CreateNHKXMLTV.py" (auto-pi-to-exe v2.5.1)\
File to be found under "output" folder. Not virus checked.

20 Jan 2019 - v1.1 - changed to pulling the file from URL

20 Jan 2019 - v1.0.5 - add second category (genre) for channels which have it

20 Jan 2019 - v1.0.4 - corrected <category> (genre) to use all lowercase

20 Jan 2019 - v1.0.3 - corrected <Icon> typo

19 Jan 2019 - v1.0.2 - added header, version, licence, and reference URL for later

19 Jan 2019 - v1.0.1 - Some tidying up

19 Jan 2019 - v1.0 - First release
