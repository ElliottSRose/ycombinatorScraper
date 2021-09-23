#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

    def checkAttribute(self, attr):
        if hasattr(self, attr):
            return getattr(self, attr)
        else:
            return setattr(self, attr, 0)

    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    def setTitleLength(self):
        self.titleLength = len(self.title.split())

    def getTitleLength(self):
        return self.checkAttribute("titleLength")

    def setOrderNum(self, orderNum):
        self.orderNum = orderNum

    def getOrderNum(self):
        return self.checkAttribute("orderNum")

    def setNumComments(self, numComments):
        self.numComments = numComments

    def getNumComments(self):
        return self.checkAttribute("numComments")

    def setPoints(self, points):
        self.points = points

    def getPoints(self):
        return self.checkAttribute("points")


class Scraper:
    #Scrape data using beautiful soup methods and create our lists
    page = requests.get("https://news.ycombinator.com/")
    soup = BeautifulSoup(page.content, 'lxml')

    def __init__(self):
        self.objList = []
        self.longerThan= []
        self.lessThan = []

    def attachOrderNum(self, entry, obj):
        obj.setOrderNum(entry.find('span','rank').text)

    def attachTitle(self, entry, obj):
        obj.setTitle(entry.find('a','storylink').text)

    def formatData(self, data):
        # pull text out of tag, split into list to get number, and format as int
        # if there is a valid entry it, will have a number and a word, therfore length>1
        if(len(data.text.split())>1):
            return int(data.text.split()[0])
        else:
            return 0

    def attachTitleLen(self, obj):
        obj.setTitleLength()

    def attachPoints(self, entry, obj):
        # load the point count onto our object
        data = entry.next_sibling.find('span','score')
        if(data):
            data = self.formatData(data)
            obj.setPoints(data)
        else:
            obj.setPoints(0)

    def attachNumComments(self, entry, obj):
        data = entry.next_sibling.select('a:nth-of-type(3)')
        if(data):
            # use index because list of 1 is returned from nth type
            data = self.formatData(data[0])
            obj.setNumComments(data)
        else:
            obj.setNumComments(0)


    def setAttributes(self, entry, obj):
        # add all of a the required attributes to our item object
        self.attachOrderNum(entry, obj)
        self.attachTitle(entry, obj)
        self.attachTitleLen(obj)
        self.attachPoints(entry, obj)
        self.attachNumComments(entry,obj)

    def getEntries(self):
        # pull the entries on ycombinator
        return self.soup.find_all('tr','athing')

    def printPost(self, item):
        print("Title: ", item.getTitle())
        print("Original Rank: ", item.getOrderNum())
        print("Points: ", item.getPoints())
        print("Comments: ", item.getNumComments())
        print("\n")

    def createBaseList(self):
        # create a list of the first 30 entries
        entry = self.getEntries()
        for i in range(30):
            item = Item()
            self.setAttributes(entry[i], item)
            self.objList.append(item)

    def printBaseList(self):
        print('First 30 posts from ycombinator'.upper())
        count = 1
        for i in self.objList:
            self.printPost(i)
            count += 1

    def longerThanFive(self):
        # build the longer than 5 word title list ordered by commments
        for i in self.objList:
            if(i.getTitleLength()>5):
                self.longerThan.append(i)
        self.longerThan.sort(key=lambda x: x.numComments, reverse=True)

    def getLongerThanFive(self):
        # print the longer than five word title list
        self.longerThanFive()
        print('Entries with more than five words in title, ordered by number of comments \n'.upper())
        count=1
        for i in self.longerThan:
            print("Rank by number of comments: ", count)
            self.printPost(i)
            count+=1

    def lessThanFive(self):
        # build the less than five word title list ordered by points
        for i in self.objList:
            if(i.getTitleLength()<=5):
                self.lessThan.append(i)
        self.lessThan.sort(key=lambda x: x.points, reverse=True)


    def getLessThanFive(self):
        # print the less than five word title list
        self.lessThanFive()
        print('Entries with less than five words in title, ordered by number of points \n'.upper())
        count=1
        for i in self.lessThan:
            print("Rank by number of points: ", count)
            self.printPost(i)
            count+=1


if __name__ == "__main__":
    S = Scraper()
    S.createBaseList()
    S.printBaseList()
    S.getLongerThanFive()
    S.getLessThanFive()
