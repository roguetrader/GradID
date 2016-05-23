import requests
requests.packages.urllib3.disable_warnings()
import json
from datetime import datetime


def store_rfid():

        url = 'https://gradrfid.table.core.windows.net/gradrfid?st=2016-05-10T16%3A09%3A00Z&se=2090-05-11T16%3A09%3A00Z&sp=raud&sv=2015-04-05&tn=gradrfid&sig=tA427WQOZnAM2BfJIHXA4SbtHLfNY%2BmNxJUV4F1ARYA%3D'
        headers = {'Accept':'application/json;odata=nometadata'}
        r = requests.get(url, headers=headers)
        a= r.text
        f = open('json.txt','w')
        f.write(a)
        f.close()
        print "Data Saved!!"

tstart = datetime.now()
store_rfid()
tstop = datetime.now()
print "Data download taken :" +  str(tstop-tstart) + "s"
