import sys
conditions = sys.argv[1].split(",")

dataFile = open('WBC.data','r').read()
dataDic = {i.split(',')[0]: i.split(',')[1:] for i in dataFile.split('\n')}
benign = []
malignant = []
for key, value in dataDic.items():
    for i in value:
        if value[-1] == "malignant":
            malignant.append(value)
            break
        else:
            benign.append(value)
            break

missing_values=0

def funDataClean():
    global dataDic
    global missing_values
    toplayici=[]
    toplam = 0
    toplam2 = 0
    i, t, k = 0, 0, 0
    ilk = 1
    y = len(malignant)
    u = len(benign)
    while ilk < 10:
        for key, value in dataDic.items():
            if "?" in value[i]:
                for anahtar, deger in dataDic.items():
                    if deger[-1] == "malignant":
                        for j in deger[i]:
                            if deger[i] == "?":
                                t += 1
                                break
                            else:
                                toplam += int(deger[i])
                                break
                    elif deger[-1] == "benign":
                        for j in deger[i]:
                            if deger[i] == "?":
                                k += 1
                                break
                            else:
                                toplam2 += int(deger[i])
                                break
                missing_values = k+t
                Av = toplam / (y - t)
                Av1 = toplam2 / (u - k)
                yuvarlama = round(Av)
                yuvarlama2 = round(Av1)
                for key, value in dataDic.items():
                    if "?" in value[i] and value[-1] == "malignant":
                        value[i] = str(yuvarlama)
                        toplayici.append(yuvarlama)
                    elif "?" in value[i] and value[-1] == "benign":
                        value[i] = str(yuvarlama2)
                        toplayici.append(yuvarlama2)
                toplam = 0
                toplam2 = 0
                break
            else:
                continue
        i += 1
        ilk += 1
    son = sum(toplayici)/missing_values
    return son
print('The average of all missing values is  : ' + '{0:.4f}'.format(funDataClean()))


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


performStepWiseSearch(sys.argv[1])
case_malignant= {}
case_benign= {}
for anahtar,value in dataDic.items():
    if value[9] == "benign":
        case_benign[anahtar]=value
    if value[9] == "malignant":
        case_malignant[anahtar]=value

print('\nTest Results:\n'
      '----------------------------------------------'
      '\nPositive (malignant) cases            : ' + str(len(case_malignant)) +
      '\nNegative (benign) cases               : ' + str(len(case_benign)) +
      '\nThe probability of being positive     : ' + '{0:.4f}'.format(len(case_malignant)/len(dataDic)) +
      '\n----------------------------------------------')



