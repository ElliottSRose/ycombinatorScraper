#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from unittest.mock import Mock
from Scraper import Item, Scraper

class TestItem(unittest.TestCase):

    def setUp(self):
        self.item = Item()

    def test_checkAttribute(self):
        #  used on titleLength, orderNum, numComments, points
        self.item.title = "Some Title"
        self.assertEqual(self.item.checkAttribute("title"),"Some Title")

    def test_setTitle(self):
        self.item.setTitle("Some Title")
        self.assertEqual(self.item.title,"Some Title")

    def test_getTitle(self):
        self.item.title = "Some Title"
        self.assertEqual(self.item.getTitle(),"Some Title")

    def test_setTitleLength(self):
        self.item.title ="Some Title"
        self.item.setTitleLength()
        self.assertEqual(self.item.titleLength, 2)

    def test_getTitleLength(self):
        self.item.titleLength = 5
        self.assertEqual(self.item.getTitleLength(), 5)

    def test_setOrderNum(self):
        self.item.setOrderNum(5)
        self.assertEqual(self.item.orderNum, 5)

    def test_getOrderNum(self):
        self.item.orderNum = 5
        self.assertEqual(self.item.getOrderNum(), 5)

    def test_setNumComments(self):
        self.item.setNumComments(5)
        self.assertEqual(self.item.numComments, 5)

    def test_getNumComments(self):
        self.item.numComments = 5
        self.assertEqual(self.item.getNumComments(), 5)

    def test_setPoints(self):
        self.item.setPoints(5)
        self.assertEqual(self.item.points, 5)

    def test_getPoints(self):
        self.item.points = 5
        self.assertEqual(self.item.getPoints(), 5)


class TestScraper(unittest.TestCase):

    def setUp(self):
        self.mock = Mock()
        self.objList = []
        self.longerThan= []
        self.lessThan = []
        self.item = Item()

    def test_attachOrderNum(self):
        self.mock.find('span','rank').text = '1'
        Scraper.attachOrderNum(self, self.mock, self.item)
        self.assertEqual(self.item.orderNum, self.mock.find('span','rank').text)

    def test_attachTitle(self):
        self.mock.find('a','storylink').text = 'Some Title'
        Scraper.attachTitle(self, self.mock, self.item)
        self.assertEqual(self.item.title, self.mock.find('a','storylink').text)

    def test_formatData(self):
        # pull text out of tag, split into list to get number, and format as int
        # if there is a valid entry it, will have a number and a word, therfore length>1
        self.mock.text = "1 World"
        self.assertEqual(Scraper.formatData(self, self.mock), 1)

        self.mock.text = "Hello"
        self.assertEqual(Scraper.formatData(self, self.mock), 0)

    def test_attachTitleLen(self):
        self.item.title = "Some Title"
        Scraper.attachTitleLen(self, self.item)
        self.assertEqual(self.item.titleLength, 2)

    def test_attachPoints(self):
        pass
        # self.mock.next_sibling.find('span','score').return_value = "100 points"
        # Scraper.attachPoints(Scraper(), self.mock, self.item)
        # self.assertEqual(self.item.points, 100)

    def test_attachNumComments(self):
        pass

    def test_setAttributes(self):
        # only calls other tested methods
        pass

    def test_getEntries(self):
        # calls beautiful soup
        pass

    def test_createBaseList(self):
        pass

    def test_longerThanFive(self):
        ob1= Item()
        ob2= Item()
        ob1.titleLength = 6
        ob1.numComments = 30
        ob2.titleLength = 8
        ob2.numComments = 5
        self.objList.extend([ob1, ob2])
        Scraper.longerThanFive(self)
        self.assertEqual(len(self.longerThan), 2)

    def test_getLongerThanFive(self):
        pass

    def test_lessThanFive(self):
        ob1= Item()
        ob2= Item()
        ob1.titleLength = 3
        ob1.points = 30
        ob2.titleLength = 4
        ob2.points = 5
        self.objList.extend([ob1, ob2])
        Scraper.lessThanFive(self)
        self.assertEqual(len(self.lessThan), 2)

    def test_getLessThanFive(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
