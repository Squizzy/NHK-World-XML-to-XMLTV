import xml.etree.ElementTree as xml
import sys

# root = xml.Element("Programme")
# root.attrib = "This year"
# programmeStart = xml.SubElement(root, "start")
# programmeStart.text = "2011"
# programmeEnd = xml.SubElement(root, "end")
# programmeEnd.text = "2013"
#
# tree = xml.ElementTree(root)
# for child in root:
#     print(root.attrib, child.tag, child.text, child.attrib)

# xml_data=tree.write()

# print(xml_data)
# for sub in root:
#     print(sub.value)


root1 = xml.Element('tv')
# root1.attrib = '''source-data-url="https://api.nhk.or.jp/nhkworld/epg/v6/world/all.json?apikey=EJfK8jdS57GqlupFgAfAAwr573q01y6k" source-info-name=“NHK World EPG Json“ source-info-url="https://www3.nhk.or.jp/nhkworld/"'''
root1.set('source-data', 'RooR1AttRiB')
root1.text = "this is the root place"
channel1 = xml.SubElement(root1, 'channel')
channel1.set('lang', 'en')
# channel1.attrib = 'id="nhk.world"'
# channel1DN = xml.SubElement(channel1, 'display-name')
# channel1DN.text = 'NHK WORLD'
# channel1ico = xml.SubElement(channel1, 'icon')
# channel1ico.attrib = 'src="https://www3.nhk.or.jp/nhkworld/assets/images/icon_nhkworld_tv.png"'
# prog1 = xml.SubElement(root1, 'Programme')
# prog1.attrib = ' start=“YYYYMMDDHHMMSS +0000" stop=“YYYYMMDDHHMMSS +0000" channel=“nhk.world”'
# prog1det1 = xml.SubElement(prog1, 'title')
# prog1det1.attrib = 'lang="en"'
# prog1det1.text = 'Now on PBS'

# tree1 = xml.ElementTree(root1)
# print(root1.tag, root1.attrib, root1.text)
# for child in root1:
#     print("\t", child.tag, child.attrib, child.text)
#     for child1 in child:
#         print("\t", "\t", child1.tag, child1.attrib, child1.text)
# print(tree1) # doesn't work
# tree1.write(sys.stdout)  # doesn't work
# root2 = xml.Element('tv')
xml.dump(root1)
