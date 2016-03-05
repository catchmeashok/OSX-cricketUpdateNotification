import urllib2,os
import time
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
def getMatchURL():
    #live RSS feeds
    f = urllib2.urlopen("http://static.cricinfo.com/rss/livescores.xml")
    root = ET.parse(f)
    print root
    channel = root.findall("channel")
    items = channel[0].findall("item")
    for i in range(0,len(items)):
        print str(i+1)+")",items[i].find("title").text
    index = raw_input("Select the match that you want update for:\n")
    #return particular match url
    return items[int(index)-1].find("link").text

def scrap(url):
    f =urllib2.urlopen(url)
    soup = BeautifulSoup(f.read())
    desc = soup.findAll(attrs={"name":"keywords"})
    team = desc[0]['content'].encode('utf-8')
    team = team.split(",",1)[0]
    score,tail,info = str(soup.title.contents[0]).partition('(')
    info,middle,tail = info.partition(')')
    score += info
    message = "terminal-notifier -title '"+team+"' -message '"+score+"' -appIcon icc.png -open '"+url+"'"
    print message
    os.system(message)
if __name__ == '__main__':
    url = getMatchURL()
    timeout = raw_input("Enter timeout in seconds\n")
    url = url.split("?",1)[0]
    while 1:
        scrap(url)
        time.sleep(int(timeout))