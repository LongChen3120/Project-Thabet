def xuLy(toDay):
    doc = open("D:/Ku/2.0/2.10/duLieuThaBet/" + toDay + ".txt", 'r')
    readLines = doc.readlines()
    doc.close()
    listKQ = []
    for x in readLines:
        listKQ.append(x[-3:])
    return listKQ



