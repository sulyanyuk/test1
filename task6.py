import math

print('Вводите точки в формате {X,Y}, введите пустую строку для подсчета')

s = 0
countedCoords = []
while True:
    n = input().split(',')
    if n == ['']:
        break
    elif len(n) == 2:
        try:
            n[0] = float(n[0])
            n[1] = float(n[1])
            if  countedCoords.count(n) == 0:
                if (0 < n[0] < math.pi) and 0 < n[1] < math.sin(n[0]):
                    s+=1
                countedCoords.append(n)
        except:
            pass

print(s)