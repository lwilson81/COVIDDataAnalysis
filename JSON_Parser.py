import json
import csv
from pprint import pprint
json2dict = json.load(open('Covid_Data.json', 'r'))
dictList = []
for i in json2dict:
    strDate = str(i['date'])
    i['date'] = strDate[2:4] +  '-' + strDate[4:6] + '-' + strDate[6::] 
    if i['death'] == None:
        i['death'] = 0
    if i['positive'] == None:
        i['positive'] = 0
    if i['hospitalized'] == None:
        i['hospitalized'] = 0
    if i['negative'] == None:
        i['negative'] = 0
    cleanedDict = {"state":i["state"], "positive":i['positive'], "negative":i['negative'], 'hospitalized':i['hospitalized'], 'death':i['death'], 'date':i['date']}
    dictList.append(cleanedDict)
dictList.sort(key = lambda x: x['state'])
with open("cleaned_JSON.csv","w") as newFile:
    dw = csv.DictWriter(newFile, fieldnames = dictList[0].keys())
    dw.writeheader()
    dw.writerows(dictList)