#! Python
# (C) 2020 Novus Space

def toIntList(rawList):
    for i in range(0, len(rawList)):
        rawList[i] = int(rawList[i])
    return rawList

def toStrList(rawList):
    for i in range(0, len(rawList)):
        rawList[i] = str(rawList[i])
    return rawList