#python code for parsing of xml files and importing it
import csv
import requests
import xml.etree.ElementTree as ET

def loadRSS():
    #url of the site
    url = 'http://www.hindustantimes.com/rss/topnews/rssfeed.xml'

    #creating HTTP request
    resp = requests.get(url)

    #save the xml file
    with open('topnewsfeed.xml','wb') as f:
        f.write(resp.content)


def parseXML(xmlfile):
     tree = ET.parse(xmlfile)

     root = tree.getroot()

     #creating list for news items
     newsitems = list()

     for items in root.findall('./channel/item'):   #path address the xml document
         #empty news dict
        news = {}

#special checking for namespace object containing media.
        for child in items:
            if child.tag == '{https://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                try:
                    news[child.tag]= child.text.encode('utf8')
                except:
                    news[child.tag]= 'empty'


        newsitems.append(news)

        return newsitems

def savetocsv(newsitems, filename):
     #specify the fields
     fields = ['guide','title','pubDate','description','link']

     #writing to csv file
     with open(filename,'w') as csvfile:

         writer = csv.DictWriter(csvfile,fieldnames = fields)

         writer.writerows(newsitems)

def main():
    loadRSS()          #laod rss from the web
    newsitems = parseXML('topnewsfeed.xml')
    savetocsv(newsitems,'topnews.csv')

if __name__=='__main__':
    main()

