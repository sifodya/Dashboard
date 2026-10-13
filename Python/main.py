# This is a sample Python script.
from encodings import utf_8

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import discord, locale, platform, requests, news, utility
from datetime import datetime
from lxml import html
import xml.etree.ElementTree as ET

""""
if platform.system() == "Windows":
  locale.setlocale(locale.LC_ALL, 'german')
elif platform.system() == "Linux":
  locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')
else:
  locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')

"""
utility.localise()
now = datetime.now()
sectionOfDay = utility.getSectionDay(now)

morning = [0, 1, 2, 3, 4, 5, 6, 7, 8, 23]
afternoon = [9, 10, 11, 12, 13, 14, 15, 16]
evening = [17, 18, 19, 20, 21, 22]
#sectionOfDay = []
if now.hour in morning:
  sectionOfDay = morning
elif now.hour in afternoon:
  sectionOfDay = afternoon
elif now.hour in evening:
  sectionOfDay = evening

srfNews = requests.get('https://www.srf.ch/news/bnf/rss/19032223')
with open('srf.xml', 'wb') as f: #except block
  f.write(srfNews.content)

tree = ET.parse('srf.xml')
root = tree.getroot()

with open('P://Documents//Git Repo//Dashboard//index.html', "r+", encoding='utf_8') as m:
  masterHTML = html.fromstring(m.read())

  childs = masterHTML[1][8].getchildren()
  for child in childs:
    if child.tag != 'p':
      child.getparent().remove(child)

  for child in root.iter('item'):
    tx = child[2].text
    if int(tx[17:19]) in sectionOfDay:
      elem4 = child[4].text
      imgLink = elem4.find('src="')
      imgLinkEnd = elem4.find('webp')
      description = elem4.find('>')

      with open('P://Documents//Git Repo//Dashboard//srfNewsTemplate.html', 'r', encoding='utf_8') as t:
        htmlTemp = html.fromstring(t.read())
      htmlTemp.set('href', child[1].text)
      htmlTemp[0][0].text = child[0].text
      htmlTemp[0][1][0].set('src', elem4[imgLink+5:imgLinkEnd+4])
      htmlTemp[0][2][0].text = child[2].text
      htmlTemp[0][2][1].text = elem4[description+1:]
      masterHTML[1][8].append(htmlTemp)
with open('P://Documents//Git Repo//Dashboard//index.html', "wb") as m:
  m.write(html.tostring(masterHTML))
