import csv
import os
import collections

# read data from csv file
def readFile(fileName):
    csvFilePath = "./data/"+fileName+".csv"
    csvFile = open(csvFilePath,'r',newline = '')
    dataset = csv.reader(csvFile)
    next(dataset)
    return dataset

readDataSet = readFile('reads')
lociDataSet = readFile('loci')

# read csv data and return two dictionaries
basePairMap = collections.defaultdict(list)
coverageCountMap = {}
for start, length in readDataSet:
    s = start                                                      
    end = str(int(start) + int(length))                            
    if (start, end) not in coverageCountMap:
      basePairMap[s] += [(start, end)]
      coverageCountMap[(start, end)] = 1
    else:
      coverageCountMap[(start, end)] += 1

# read loci.csv, return list of DNA position and write data
positionList = []
for data in lociDataSet:
    positionList.append(data[0])
titleFields = ['postion', 'coverage']
csvFile = open('./data/loci.csv', 'w', newline='')
lociDataWriter = csv.writer(csvFile)
lociDataWriter.writerow(titleFields)

# compute coverage of DNA positions
for pos in positionList:
    count = 0
    d = pos
    li = basePairMap.get(d)
    if li == None:
      lociDataWriter.writerow([pos, str(0)])
      continue
    for val in li:
      start_val = int(val[0])
      end_val = int(val[1])
      if int(pos) >= int(start_val) and int(pos) <= end_val:
        count += coverageCountMap.get((val[0], val[1]))
    lociDataWriter.writerow([pos, str(count)])