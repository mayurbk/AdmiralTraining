import xml.etree.ElementTree as ET
tree = ET.parse('employee.xml')

#getting the parent id
root = tree.getroot()

#print the root/parent tag
print(root)

#print the first attributes of the tag
print(root[1].attrib)

#print the text containde within the first subtag
print(root[2][1].text)
for child in root:
    print(child.tag,child.attrib)