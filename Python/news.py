import requests
from lxml import html
import xml.etree.ElementTree as ET

def getNewsRSS(u):
  """

  :param u: The URL of the news rss feed
  :type u: str
  :return: The root of the news rss feed
  """
  srfNews = requests.get(u)
  with open('srf.xml', 'wb') as f:  # except block
    f.write(srfNews.content)

  tree = ET.parse('srf.xml')
  root = tree.getroot()
  return root
