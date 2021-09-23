# ycombinatorScraper
This program will pull the first 30 entries from ycombinator, creating objects that keep the order-number, points, number of comments, title, and the title length for each one. These are all then collected and stored in a list. Finally two filter and sorting functions will be applied:

Entries with more than five words in the title ordered by the number of comments first.
Entries with less than or equal to five words in the title ordered by points.

The scraper requires requests and BeautifulSoup - File can be ran from the terminal via command: python3 Scraper.py
This file will first print the 30 entries from ycombinator in order. Then it will print the two filtered lists in their new orders. 

The test file uses python's built in unittest framework. Testing can be ran from the terminal via command: test_Scraper.py
You'll see some of these tests were skipped as I have not had time to get to them yet. 
