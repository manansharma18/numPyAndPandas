import json
import urllib.request

def printData(data):
    theJSON = json.load(data)
    #print(theJSON)
    if theJSON['metadata'] != None:
            #print(theJSON)
        for i in theJSON['features']:
           print(str(i['properties']))
    
def main():

    url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    metData= urllib.request.urlopen(url)
    if metData.getcode() == 200:
        print ("Link is valid")
        printData(metData)

if __name__=="__main__":
    main()