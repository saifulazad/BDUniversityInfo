__author__ = 'azad'

from bs4 import BeautifulSoup
import requests

from Table_data import getTableData
from Basic_info import BasicInfo
for x in range(10,1001):

    url = 'http://www.eduicon.com/Subject/%s.html' % x
    print  url
    payload = {
        'q': 'Python',
    }
    r = requests.get(url % payload)

    soup = BeautifulSoup(r.text, "html5lib")


    titles = soup.findAll( attrs={'class': 'content-box'})

    rows = titles[0]

    rowws = rows.findAll( attrs={'class': 'row'})

    ob =BasicInfo();


    ob.getBasicInfo(rowws[0])

    print ob.__dict__

    tables = rowws[3].findAll("table")


    print getTableData(tables[0])
