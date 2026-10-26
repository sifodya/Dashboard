import datetime
import locale, platform
from typing import Any


def localise():
  """
  Sets the appropriate german localisation depending on the platform
  :return: Nothing
  :rtype: None
  """
  if platform.system() == "Windows":
    locale.setlocale(locale.LC_ALL, 'german')
  elif platform.system() == "Linux":
    locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')
  else:
    locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')

def getSectionDay(d: datetime.date) -> list[int] | list[Any]:
  """
  Takes the current date and selects the appropriate section day

  The *d* (datetime.date) is the current date and time. The time is
  used to determine if it is morning, afternoon or evening.

  :param d: current date
  :type d: datetime.date
  :return: List of integers representing the section day in hours
  :rtype: list[int]
  """
  morning = [0, 1, 2, 3, 4, 5, 6, 7, 8, 23]
  afternoon = [9, 10, 11, 12, 13, 14, 15, 16]
  evening = [17, 18, 19, 20, 21, 22]
  sectionOfDay = []
  if d.hour in morning:
    sectionOfDay = morning
  elif d.hour in afternoon:
    sectionOfDay = afternoon
  elif d.hour in evening:
    sectionOfDay = evening
  return sectionOfDay
def xmlNS(ns, t):
  """
  :param ns: XML Namespace
  :type ns: str
  :param t: XML Tag to search for
  :type t: str
  :return: combined search string
  :rtype: str
  """
  xmlTag = ns+t
  return xmlTag
