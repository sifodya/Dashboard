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

def writeNewsToHTML(d, root, sectionOfDay):
  with open(d, 'r+', encoding='utf8') as f:
    masterHTML = html.fromstring(f.read())

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
        htmlTemp[0][1][0].set('src', elem4[imgLink + 5:imgLinkEnd + 4])
        htmlTemp[0][2][0].text = child[2].text
        htmlTemp[0][2][1].text = elem4[description + 1:]
        masterHTML[1][8].append(htmlTemp)
  with open('P://Documents//Git Repo//Dashboard//index.html', "wb") as m:
    m.write(html.tostring(masterHTML))
