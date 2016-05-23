import json
from datetime import datetime
import sys


def get_grad_file_query(extid):
        ids =extid
        print "Search local data file..... ", ids
        p = datetime.now()

        f = open('json.txt')
        a = f.read()
        f.close()
        decoded = json.loads(a)
        maxlength = len(decoded['value'])

        print str(maxlength) + " records found"

        def cantfind():
                print "Cant find Graduand"
                return;

        Counter = 0
        fname = ""

        while (fname != ids):
            fname = decoded['value'][Counter]['rfid']
            Counter = Counter + 1
            if (Counter  == maxlength) and (fname!= ids):
                cantfind()
                break

        if (Counter == maxlength) and (fname != ids):
                print ""
        else:
                Counter = Counter - 1
                print "record " + str(Counter + 1) + " of " +  str(maxlength)
                print decoded['value'][Counter]['Name']

        n = datetime.now()
        print "File search taken :" + str(n-p) + "s"

