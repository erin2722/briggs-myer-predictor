import scipy
import numpy

#initialize variables
H2O2Data = []
KIO3Data = []
tempData = []

H2O2Avg = []
KIO3Avg = []
tempAvg = []
optimizedOutput = [0, 0, 0]

#average each of the data points so that it is an x, y arrary
def avgData(dataset):
    sum = 0.0
    length = 0.0
    for i in range(1, len(dataset)):
        sum += dataset[i]
        length += 1
    return sum/length

#optimize the array sent to this function
def optimize(xyDatapoints):
    x = []
    y = []
    quadRegression = []
    for i in range(0, len(xyDatapoints)):
        x.append(xyDatapoints[i][0])
        y.append(xyDatapoints[i][1])
    quadRegression = numpy.polyfit(x, y, 2)
    if quadRegression[0] > 0:
        quadRegression[0] = quadRegression[0]*-1
        quadRegression[2] = quadRegression[2]
    print(quadRegression)
    return float(numpy.roots(numpy.polyder(quadRegression)))

def isFloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

dataFile = open("data.txt", "r")
fileLines = dataFile.readlines()
for i in range(0, len(fileLines)-1):
    if fileLines[i][0] is "H":
        j = i + 1
        while isFloat(fileLines[j][0]):
            H2O2Data.append(fileLines[j][:-1].split())
            j+=1
        for k in range(0, len(H2O2Data)):
            for m in range(0, len(H2O2Data[k])):
                H2O2Data[k][m] = float(H2O2Data[k][m])
    if fileLines[i][0] is "K":
        j = i + 1
        while isFloat(fileLines[j][0]):
            KIO3Data.append(fileLines[j][:-1].split())
            j+=1
        for k in range(0, len(KIO3Data)):
            for m in range(0, len(KIO3Data[k])):
                KIO3Data[k][m] = float(KIO3Data[k][m])
    if fileLines[i][0] is "T":
        j = i + 1
        while isFloat(fileLines[j][0]):
            tempData.append(fileLines[j][:-1].split())
            j+=1
            if j >= len(fileLines):
                break
        for k in range(0, len(tempData)):
            for m in range(0, len(tempData[k])):
                tempData[k][m] = float(tempData[k][m])

for i in range(0, len(H2O2Data)):
    H2O2Avg.append([])
    H2O2Avg[i].append(H2O2Data[i][0])
    H2O2Avg[i].append(avgData(H2O2Data[i]))
for i in range(0, len(KIO3Data)):
    KIO3Avg.append([])
    KIO3Avg[i].append(KIO3Data[i][0])
    KIO3Avg[i].append(avgData(KIO3Data[i]))
for i in range(0, len(tempData)):
    tempAvg.append([])
    tempAvg[i].append(tempData[i][0])
    tempAvg[i].append(avgData(tempData[i]))

print(H2O2Avg)
optimizedOutput[0]=round(optimize(H2O2Avg), 5)
optimizedOutput[1]=round(optimize(KIO3Avg), 2)
optimizedOutput[2]=round(optimize(tempAvg), 2)

print("H2O2: " + str(optimizedOutput[0]) + "% KIO3: " + str(optimizedOutput[1]) + "mol Temperature: " + str(optimizedOutput[2]) + "°C")
