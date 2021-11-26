import snscrape.modules.reddit
import pandas as pd
import csv
import json
import requests


scraper = snscrape.modules.reddit.RedditSearchScraper('stopthesteal')
for i, item in enumerate(scraper.get_items()):
        print(item.json())
        if i>=1000:
            break