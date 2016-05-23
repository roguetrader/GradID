import requests
requests.packages.urllib3.disable_warnings()
from datetime import datetime

def get_grad_azure_query(extid):
        ids = extid
        # print "Search Azure Table Store... "
        start = datetime.now()

        url = "https://gradrfid.table.core.windows.net/gradrfid?$filter=rfid%20eq%20" + "%27" + ids + "%27" + "%20&st=2016-05-13T09%3A55%3A00Z&se=2020-05-14T09%3A55%3A00Z&sp=raud&sv=2015-04-05&tn=gradrfid&sig=Yr0yGnvXFe7C4VK3id6IuOGPtiyHnY70Q%2FU%2BVnOGn%2Bs%3D"

        headers = {'Accept':'application/json;odata=nometadata'}
        r = requests.get(url, headers=headers)
	decoded = r.json()
        maxlength = len(decoded['value'])
        if maxlength > 0 :
                print decoded['value'][0]['Name']
        else :
                print "Cant find Graduand"
        finish = datetime.now()
        # print "Azure table single row search time: " + str(finish - start) + "s"
