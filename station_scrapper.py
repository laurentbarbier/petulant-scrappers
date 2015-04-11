# -*- coding:utf-8 -*-
import urllib2
from BeautifulSoup import BeautifulSoup

f = open("wunder-data.txt", "w")

for m in range(1, 13):
    for d in range(1, 32):
        if m == 2 and d > 28:
            break
        elif m in [4, 6, 9, 11] and d > 30:
            break

        if len(str(m)) < 2:
            mStamp = '0' + str(m)
        else:
            mStamp = str(m)

        if len(str(d)) < 2:
            dStamp = '0' + str(d)
        else:
            dStamp = str(d)

        timestamp = '2014' + mStamp + dStamp
        print "Récupération des données du " + timestamp
        url = "http://www.wunderground.com/history/airport/LFPO/2014/" + mStamp + "/" + dStamp + "/DailyHistory.html"
        page = urllib2.urlopen(url)

        soup = BeautifulSoup(page)
        dayTemp = soup.findAll(attrs={"class": "wx-value"})[0].string

        f.write(timestamp + "," + dayTemp + "\n")

f.close();
