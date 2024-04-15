# Conversion of NHK's EPG in JSON to XMLTV - v1.2

Python v3 (under Python folder above)
* Only file "CreateNHKXMLTV.py" is needed (+ Python on the machine on which it is run of course)
* Requires Python 3.x
* Runs on Windows, MacOS, Linux

Python v2
* --> branch p2 implements using python v2 as per dazzhk implementation. it is not merged into master yet as it is not tested
* Requires Python 2.x
* Should on Windows, MacOS, Linux
* Any feedback on testing welcome


# Background info
NHK-World-XML-to-XMLTV
* creating XMLTV file from XML of NHK World

Source info.txt
*  path to the original info, and tools
  
all-json-example.json
*  Save of NHKWorld file with .json used
  
all-xml-example-from-using-url.xml
*  save of NHKWorld file with .XML used
  
convertjson.xml
*  json extracted from the URL converted with the online tool
  
source XML data to transform.xml
*   Unitary source of data to transform
   
NHK World XML to XMLTV converter
*  Path to the XCode CLI file to do the conversion
