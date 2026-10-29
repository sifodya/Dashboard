# This is a sample Python script.
from encodings import utf_8

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import discord, locale, platform, requests, news, utility
from datetime import datetime
from lxml import html
from bs4 import BeautifulSoup as bs
#from requests_html import HTMLSession
import xml.etree.ElementTree as ET

utility.localise()
now = datetime.now()
sectionOfDay = utility.getSectionDay(now)

#=====================================================================
#SRF
root = news.getNewsRSS('https://www.srf.ch/news/bnf/rss/19032223', 'srf.xml')

with open('..//index.html', "r+", encoding='utf_8') as m:
  masterHTML = html.fromstring(m.read())
  childs = masterHTML[1][8].getchildren()
  for child in childs:
    if child.tag != 'p':
      child.getparent().remove(child)

  for child in root.iter('item'):
    tx = child[2].text

    if int(tx[17:19]) in sectionOfDay and int(tx[5:7]) == int(now.day):
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
#=====================================================================
#Audiokinetic
"""
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36'}
blog = requests.get('https://www.audiokinetic.com/en/community/blog', headers=headers)

session = HTMLSession()
r = session.get('https://www.audiokinetic.com/en/community/blog')
r.html.render()
soup = bs(r.content, 'html.parser')
AkChilds = soup.children
for child in AkChilds:
  print(child.text)"""
#=======================================================================
#PCGamer

pcGamerRoot = news.getNewsRSS('https://www.pcgamer.com/rss/', 'pcgamer.xml')
for child in pcGamerRoot.iter('item'):
  print(child.find('pubDate').text)
  print(child.find('title').text.strip())
  print(child.find('link').text)
  print(child.find('enclosure').attrib['url'])
  print(child.find('category').text)
  print(child.find('description').text.strip())

#Gameswirtschaft
gwRoot = news.getNewsRSS('https://www.gameswirtschaft.de/feed/atom/', 'gw.xml')
nns = str(gwRoot.tag)
ns = nns[:-4]
for child in gwRoot.iter(utility.xmlNS(ns, 'entry')):
  print(child.find(utility.xmlNS(ns, 'title')).text)
  print(child.find(utility.xmlNS(ns, 'link')).attrib['href'])
  print(child.find(utility.xmlNS(ns, 'published')).text)
  summ = child.find(utility.xmlNS(ns, 'summary')).text
  s = summ.find('src')
  e = summ.find('png')
  if e == -1:
    e = summ.find('jpg')
  print(summ[s + 5:e + 3])
  sS = summ.find('/>')
  eS = summ.find('</p>')
  print(summ[sS + 2:eS - 1])

#Gameworldobserver
gwoRoot  = news.getNewsRSS('https://gameworldobserver.com/feed/atom/', 'gwo.xml')
nns = str(gwoRoot.tag)
ns = nns[:-4]
for child in gwoRoot.iter(utility.xmlNS(ns, 'entry')):
  print(child.find(utility.xmlNS(ns, 'title')).text)
  print(child.find(utility.xmlNS(ns, 'link')).attrib['href'])
  print(child.find(utility.xmlNS(ns, 'published')).text)
  print(child.find(utility.xmlNS(ns, 'summary')).text)
  imageStr = child.find(utility.xmlNS(ns, 'content')).text
  s = imageStr.find('src')
  e = imageStr.find('png')
  if e == -1:
    e = imageStr.find('jpg')
  print(imageStr[s + 5:e + 3])
  print(child.find(utility.xmlNS(ns, 'category')).attrib['term'])
