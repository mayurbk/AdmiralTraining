# from bs4 import BeautifulSoup
# #step1 - finding tags   step2 - extracting from the tags
# #read the data inside the xml to a variable
# with open('employee.xml','r') as f:
#     data = f.read()
# #passing the stored data inside the beautiful parser
# Bs_data = BeautifulSoup(data, 'xml')
#
# #finding all instances of a tag
# b_id = Bs_data.find('email')
# print(b_id)

import xml.etree.ElementTree as ET
#
# tree = ET.parse('employee.xml')
# root = tree.getroot()
# print(root.findall('row'))

# import xml.etree.ElementTree as ET
#
# tree = ET.parse('employee.xml')
# root = tree.getroot()
# # print(root[0][0].text)
#
# for books in root.findall("row"):
#     title = books.find('email').text
#     print(title)


