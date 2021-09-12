import csv
with open('states_history.csv',encoding = 'utf8') as infile:
    reader = csv.reader(infile)
    readerlist = [line for line in reader]
fixedlist =[]
for eachlist in readerlist:
    eachlist = eachlist[0:20]
    del eachlist[13:19]
    del eachlist[7:12]
    del eachlist[3:6]
    fixedlist.append(eachlist)

headers = fixedlist[0]
data = fixedlist[1::]
amendedlist = []
for eachlist in data:
    if eachlist[2] == '':
        eachlist[2] = 'No Data'
    else:
        eachlist[2] = int(eachlist[2])

    if eachlist[3] == '':
        eachlist[3] = 'No Data'
    else:
        eachlist[3] = int(eachlist[3])

    if eachlist[4] == '':
        eachlist[4] = 'No Data'
    else:
        eachlist[4] = int(eachlist[4])

    if eachlist[5] == '':
        eachlist[5] = 'No Data'
    else:
        eachlist[5] = int(eachlist[5])
    amendedlist.append(eachlist)
amendedlist.sort(key = lambda x: x[1])
for eachline in amendedlist:
    dateComp = eachline[0].split('-')
    if dateComp[1][0] == '0':
        dateComp[1] = dateComp[1][-1]
    if dateComp[2][0] == '0':
        dateComp[2] = dateComp[2][-1]
    date = dateComp[1]+'/'+dateComp[2]+'/'+dateComp[0]
    eachline[0] = date
with open("cleaned_CSV.csv","w") as newFile:
    writer = csv.writer(newFile)
    writer.writerows(amendedlist)





