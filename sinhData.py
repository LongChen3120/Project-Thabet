import random as rd
for x in range(31):
    a = []
    ghi = open('D:/Ku/2.0/2.10/duLieu/' + str(x) +  '.txt', 'w')
    for y in range(1000):
        b = rd.randint(00, 99)
        ghi.write(str(b) + "\n")
    ghi.close()
