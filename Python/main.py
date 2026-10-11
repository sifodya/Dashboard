# This is a sample Python script.
from encodings import utf_8

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import discord, locale, platform, requests
from datetime import datetime
from lxml import html, etree
import xml.etree.ElementTree as ET

if platform.system() == "Windows":
  locale.setlocale(locale.LC_ALL, 'german')
elif platform.system() == "Linux":
  locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')
else:
  locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')

now = datetime.now()
srfNews = requests.get('https://www.srf.ch/news/bnf/rss/19032223')
with open('srf.xml', 'wb') as f: #except block
  f.write(srfNews.content)

tree = ET.parse('srf.xml')
root = tree.getroot()

#for child in root:
  #print (child.tag, child.attrib)

#print(root[0][6])

with open('P://Documents//Git Repo//Dashboard//index.html', "r+", encoding='utf_8') as m:
  masterHTML = html.fromstring(m.read())

  childs = masterHTML[1][8].getchildren()
  for child in childs:
    masterHTML.remove(child)
  #for i in range(1, len(childs)):
  #  print(i)
  #  masterHTML.remove(masterHTML[1][8][i])
  #masterHTML[1][8][1].clear()
  #print(html.tostring(masterHTML[1][8]).decode())
  for child in root.iter('item'):
    elem4 = child[4].text
    imgLink = elem4.find('src="')
    imgLinkEnd = elem4.find('webp')
    description = elem4.find('>')
    #print(elem4[imgLink+5:imgLinkEnd+4])
    #print(elem4[description+1:])
    #print(child[0].text) #titel
    #print(child[1].text) #link
    #print(child[2].text) #date
    #print(child[4].text)

    with open('P://Documents//Git Repo//Dashboard//srfNewsTemplate.html', 'r', encoding='utf_8') as t:
      htmlTemp = html.fromstring(t.read())
    htmlTemp.set('href', child[1].text)
    htmlTemp[0][0].text = child[0].text
    htmlTemp[0][1][0].set('src', elem4[imgLink+5:imgLinkEnd+4])
    htmlTemp[0][2][0].text = child[2].text
    htmlTemp[0][2][1].text = elem4[description+1:]
    masterHTML[1][8].append(htmlTemp)
  #print(html.tostring(masterHTML[1][8]).decode())
with open('P://Documents//Git Repo//Dashboard//index.html', "wb") as m:
  m.write(html.tostring(masterHTML))
