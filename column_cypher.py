"""
Column Cypher
By Ian Kruper

"""

def encrypter(message):
    m1 = message
    space = ""

    while len(m1) % 6 != 0:
        m1 += " "
        
    r1 = (m1[0:len(m1)/2])
    r2 = (m1[len(m1)/2:len(m1)])
    
    rsum1 = ""
    for number in range(0,len(r1)):
        rsum1 += (r1[number])
        rsum1 += (r2[number])
        
    m2 = space.join(rsum1)    
    
    r3 = (m2[0:len(m2)/3])
    r4 = (m2[len(m2)/3:2*len(m2)/3])
    r5 = (m2[2*len(m2)/3:len(m2)])
    
    rsum2 = ""
    for number in range(0,len(r3)):
        rsum2 += (r3[number])
        rsum2 += (r4[number])
        rsum2 += (r5[number])
    
    m3 = space.join(rsum2)
    m3 += "xjjquxy"
    return m3

def decrypter(message):
    m3 = message[0:len(message)-7]
    space = ""    
    r2 = []
    
    r2.append(m3[0:len(message):3])
    r2.append(m3[1:len(message):3])
    r2.append(m3[2:len(message):3])
    
    m2 = space.join(r2)
    
    r1 = []
    
    r1.append(m2[0:len(m2):2])
    r1.append(m2[1:len(m2):2])
    
    m1 = space.join(r1)
        
    return m1
