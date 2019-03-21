#!/usr/bin/env python2

#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import sys
import requests

# if __name__ == '__name__'

def checkInstance(instance_name):
     try:
          r = requests.head('https://' + instance_name + '.service-now.com/stats.do')
          print(instance_name + ": " + str(r.status_code))
     except requests.ConnectionError:
          print(instance_name + ": failed to connect")

checkInstance(sys.argv[1])
