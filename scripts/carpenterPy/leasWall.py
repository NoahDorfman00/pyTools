import math

def findPieces(longs, shorts):
    pieces = []
    for i in range(len(longs)):
        if longs[i]==-1:
            continue
        for j in range(len(shorts)):
            if i==j or shorts[j]==-1:
                continue
            if (longs[i] + shorts[j] + ((longs[j]-shorts[j])/2)) <= woodLen:
                pieces.append([longs[i], shorts[j]])
                longs[i] = -1
                shorts[i] = -1
                longs[j] = -1
                shorts[j] = -1
                break
    for short in shorts:
        if short != -1:
            pieces.append([0.0, short])
    for long in longs:
        if long != -1:
            pieces.append([long, 0.0])

    return pieces

woodLen = 96.0
w = 97
h = 114
theta = math.atan(h/w)
theta2 = (math.pi/2) - theta

print("Angles: ", str(math.degrees(theta)) + ", " + str(math.degrees(theta2)))

hypShort = 2.5 / math.sin(theta)
btwnShort = (w - hypShort) / 9

hypLong = 2.5 / math.sin(theta2)
btwnLong = (h + hypLong) / 9 

print("Hyps: ", str(hypShort) + ", " + str(hypLong))

print("--- Short Sides ---")
shorts = []
longs = []
legA = w/2
legB = h/2
for i in range(5):
    hyp = math.sqrt(legA**2 + legB**2)
    for j in range(4):
        longs.append(hyp)
    print("long: ", hyp)
    hyp = math.sqrt((legA-hypShort)**2 + (legB-hypLong)**2)
    for j in range(4):
        shorts.append(hyp)
    print("short: ", hyp)
    legA -= btwnShort
    legB -= btwnShort 

shortSide = findPieces(longs, shorts)
for piece in shortSide:
    print(piece)          
print("--- Long Sides ---")
shorts = []
longs = []
legA = w/2
legB = ((h/2) + hypLong) - btwnLong
for i in range(4):
    hyp = math.sqrt(legA**2 + legB**2)
    for j in range(4):
        longs.append(hyp)
    print("long: ", hyp)
    hyp = math.sqrt((legA-hypShort)**2 + (legB-hypLong)**2)
    for j in range(4):
        shorts.append(hyp)
    print("short: ", hyp)
    legA -= btwnLong
    legB -= btwnLong

longSide = findPieces(longs, shorts)
for piece in longSide:
    print(piece)

print("--- Total ---")

print(len(longSide) + len(shortSide), "8-ft pieces")

