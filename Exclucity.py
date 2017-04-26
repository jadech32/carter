import requests
from bs4 import BeautifulSoup as bs
from scraper import *
from carter import *
from datetime import datetime

time1 = datetime.now()
checkout(link_finder(),0)
time2 = datetime.now()
delta = time2 - time1
print("Total Time: " + str(delta.total_seconds()) + "s")
