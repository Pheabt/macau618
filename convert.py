#! usr/bin/env python

from sys import argv
import os
from os.path import exists
import json
import pandas as pd
import math
import numpy as np
import copy
import csv
import time
import datetime
import pandas as pd

path = os.path.dirname(os.path.abspath(__file__))

coord_file=open(path+"/(0716)coor_officeandhome1706.csv", "r", encoding="utf-8")
coord_reader = csv.reader(coord_file, delimiter=',')

output_file="(0716)cases.csv"

df_csv = pd.read_csv(path+"/COVID20220618-澳門確診個案_20220716_1500_vac.csv", encoding="utf-8", index_col="序號")

# output_name=path+"/(0710)cases.csv"
# if os.path.exists(output_name):
#     os.remove(output_name)

#geojson_file=open(path+"/(0711)geodata_cases.json", "w", encoding="utf-8")

entry = {
    "name":"",
    "lat":"",
    "lng":"",
    "type":"Feature",
    "properties":{},
    # "properties":d,
}

geojs={
    "type": "FeatureCollection",
    "features":[
    ]  
}

# output_file=open(output_name, "a", encoding="utf-8")
# output_file.write("lon,lat,time"+"\n")

df = pd.DataFrame(columns=['lat','lon','timestamp'])

next(coord_reader)
for d in coord_reader:
    time_string=d[7]
    if time_string.split("/")[0]=='2022':
        time_int=time.mktime(datetime.datetime.strptime(time_string, "%Y/%m/%d").timetuple())
    else:
        time_int=time.mktime(datetime.datetime.strptime(time_string, "%m/%d/%Y").timetuple())

    id=int(d[0])
    lon_w=d[2]
    lat_w=d[3]
    lon=d[5]
    lat=d[6]

    if lon!='' and lat!='':
        dict = {'lon':lon, 'lat': lat, 'timestamp': time_int}
        df.loc[df.shape[0]]=dict
        #output_file.write(lon+","+lat+","+str(time_int)+"\n")

    if lon_w!='' and lat_w!='':
        if df_csv.loc[id]["職業"]!='學生':
            dict = {'lon':lon_w, 'lat': lat_w, 'timestamp': time_int}
            df.loc[df.shape[0]]=dict
        #output_file.write(lon_w+","+lat_w+","+str(time_int)+"\n")

df.sort_values(by=['timestamp'], inplace=True)

df.to_csv(output_file,index=False)

#     entry["lat"]=lat
#     entry["lng"]=lon
#     entry["properties"]={'addr':d[4]}
#     geojs["features"].append(copy.deepcopy(entry))

# json.dump(geojs, geojson_file)
# geojson_file.close()
# exit()