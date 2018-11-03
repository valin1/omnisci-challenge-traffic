from pymapd import connect
import requests
import io
import pandas as pd
from datetime import datetime

import os
MAPD_STORAGE = %env MAPD_STORAGE
MAPD_ERROR_LOG = os.path.join(MAPD_STORAGE,'data/mapd_log/mapd_server.ERROR')

user_str = 'LD866694E4D9143A5A3F'
password_str = 'jh5mnhiHEJefnzZ1t4GvSKxh28bGyCjvdaTO6JoQ'
host_str = 'use2-api.mapd.cloud'
dbname_str = 'mapd'

connection = pymapd.connect(user=user_str, password=password_str, host=host_str, dbname=dbname_str, port=443, protocol='https')

url = "https://s3-us-west-1.amazonaws.com/mapd-cloud/DataSets/calhacks/uber_movement_data2.csv.gz"

def mapdql(query):
	if con is None:
		print("Connection bad or stale")
		return None
	try:
        print('Executing query: {}'.format(query))
        results = con.execute(query)
        return results
    except:
        print('Exception executing query')
        a,b,c = sys.exc_info()
        for d in traceback.format_exception(a,b,c) :
           print (d)
        return None