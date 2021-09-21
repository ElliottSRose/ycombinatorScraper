# The instructions are below for a web-crawling exercise:
#
# Using the language that you feel most proficient in, you’ll have to create a
# web crawler using scraping techniques to extract the first 30 entries from
# https://news.ycombinator.com/ . You’ll only care about the title, the number
# of the order, the number of comments, and points for each entry.​
#
# From there, we want it to be able to perform a couple of filtering operations:
#
#     Filter all previous entries with more than five words in the title ordered by the number of comments first.
#     Filter all previous entries with less than or equal to five words in the title ordered by points.
import requests
from bs4 import BeautifulSoup

class Item:
    def __init___(self):
        self.title       = title
        self.titleLength = titleLength
        self.orderNum    = orderNum
        self.numComments = numComments
        self.points      = points

    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    def setTitleLength(self):
        self.titleLength = len(self.title)

    def getTitleLength(self):
        if hasattr(self, 'title'):
            self.setTitleLength()
            return self.titleLength
        else:
            print ('Title has not been set')

    def setOrderNum(self, orderNum):
        self.orderNum = orderNum

    def getOrderNum(self):
        return self.orderNum

    def setNumCommments(self, numComments):
        self.numComments = numComments

    def getNumComments(self):
        return self.numComments

    def setPoints(self, points):
        self.points = points

    def getPoints(self):
        return self.points


class Scraper:
    page = requests.get("https://news.ycombinator.com/")
    soup = BeautifulSoup(page.content, 'lxml')
    def __init__(self):
        self.objList = []

    def attachOrderNum(self, entry, obj):
        obj.setOrderNum(entry.find('span','rank').text)
        print(obj.getOrderNum())

    def attachTitle(self, entry, obj):
        obj.setTitle(entry.find('a','storylink').text)
        print(obj.getTitle())

    def formatData(self, data):
        # pull text out of tag, split into list to get number, and format as int
        if(len(data.text.split())>1):
            return int(data.text.split()[0])
        else:
            return 0

    def attachPoints(self, entry, obj):
        data = entry.next_sibling.find('span','score')
        if(data):
            data = self.formatData(data)
            obj.setPoints(data)
            print(obj.getPoints())

    def attachNumComments(self, entry, obj):
        data = entry.next_sibling.select('a:nth-of-type(3)')
        if(data):
            # use index because list of 1 is returned from nth type
            data = data[0]
            data = self.formatData(data)
            obj.setNumCommments(data)
            print(obj.getNumComments())

    def setAttributes(self, entry, obj):
        # set order number
        self.attachOrderNum(entry, obj)
        # set title
        self.attachTitle(entry, obj)
        # set points
        self.attachPoints(entry, obj)
        # set comments
        self.attachNumComments(entry,obj)

    def getEntries(self):
        return self.soup.find_all('tr','athing')

    def createBaseList(self):
        entry = self.getEntries()
        for i in range(30):
            item = Item()
            self.setAttributes(entry[i], item)
            self.objList.append(item)


Scraper().createBaseList()
