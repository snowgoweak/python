procent = [i for i in range(0, 21)]

for procent in procent:
    if procent == 0 or procent >= 5:
        print(procent, 'процентов')
    elif procent == 1:
        print(procent, 'процент')
    elif procent >= 2 or procent <= 4:
        print(procent, 'процента')

