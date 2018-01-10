import sys

dataFile = open('WBC.data', 'r').read()
dataDic = {i.split(',')[0]: i.split(',')[1:] for i in dataFile.split('\n')}

def funDataClean():

    global dataDic

    missingValues = []

    for key, val in dataDic.items():
        for j in range(len(val)):
            if val[j] == '?':
                val[j] = calcMissing(j, val[9])
                missingValues.append(val[j])
                dataDic[key] = val

    return sum(missingValues) / len(missingValues)


def calcMissing(index, category):
    indexSum = []

    for key, val in dataDic.items():
        for k in range(len(val) - 1):
            if val[index] != '?' and val[9] == category:
                indexSum.append(int(val[index]))

    return round(sum(indexSum) / len(indexSum))

def performStepWiseSearch(args):
    global dataDic

    argl = args.split(',')
    for i in range(len(argl)):
        if argl[i] == '?':
            continue
        else:
            argt = argl[i].split(':')
            c = int(argt[1])
            if argt[0] == '<':
                dataDic = dict({k: v for k, v in dataDic.items() if int(v[i]) < c})
            if argt[0] == '<=':
                dataDic = dict({k: v for k, v in dataDic.items() if int(v[i]) <= c})
            if argt[0] == '>':
                dataDic = dict({k: v for k, v in dataDic.items() if int(v[i]) > c})
            if argt[0] == '>=':
                dataDic = dict({k: v for k, v in dataDic.items() if int(v[i]) >= c})
            if argt[0] == '!=':
                dataDic = dict({k: v for k, v in dataDic.items() if int(v[i]) != c})
            if argt[0] == '=':
                dataDic = dict({k: v for k, v in dataDic.items() if int(v[i]) == c})

print('The average of all missing values is  : ' + '{0:.4f}'.format(funDataClean()))

performStepWiseSearch(sys.argv[1])

caseMalignant = len(dict({k: v for k, v in dataDic.items() if v[9] == 'malignant'}))
caseBenign = len(dict({k: v for k, v in dataDic.items() if v[9] == 'benign'}))

print('\nTest Results:\n'
      '----------------------------------------------'
      '\nPositive (malignant) cases            : ' + str(caseMalignant) +
      '\nNegative (benign) cases               : ' + str(caseBenign) +
      '\nThe probability of being positive     : ' + '{0:.4f}'.format(caseMalignant / len(dataDic)) +
      '\n----------------------------------------------')
