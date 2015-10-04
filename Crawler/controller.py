__author__ = 'nimbus'
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen(url="https://pythonhosted.org/py2app/")
print(html.read())