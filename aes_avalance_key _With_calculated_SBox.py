def multi(a,b):
    removeBitXor = 256
    xorBit = 27
    inTwo = '{0:08b}'.format(b)
    #print(inTwo)
    #print(inTwo[6])
    #print(inTwo[7])
    
    bitValueZero = a
    #print(bitValueZero)
    inOne = '{0:08b}'.format(bitValueZero)
    #print(inOne)
    
    bitValueOne = a << 1
    if(bitValueOne >255):
        temp = bitValueOne ^ removeBitXor
        bitValueOne = temp
        temp = bitValueOne ^ xorBit
        bitValueOne = temp
    #print(bitValueOne)
    inOne = '{0:08b}'.format(bitValueOne)
    #print(inOne)
    
    bitValueTwo = bitValueOne << 1
    if(bitValueTwo >255):
        temp = bitValueTwo ^ removeBitXor
        bitValueTwo = temp
        temp = bitValueTwo ^ xorBit
        bitValueTwo = temp
    #print(bitValueTwo)
    inOne = '{0:08b}'.format(bitValueTwo)
    #print(inOne)

    bitValueThree = bitValueTwo << 1
    if(bitValueThree >255):
        temp = bitValueThree ^ removeBitXor
        bitValueThree = temp
        temp = bitValueThree ^ xorBit
        bitValueThree = temp
    #print(bitValueThree)
    inOne = '{0:08b}'.format(bitValueThree)
    #print(inOne)

    bitValueFour = bitValueThree << 1
    if(bitValueFour >255):
        temp = bitValueFour ^ removeBitXor
        bitValueFour = temp
        temp = bitValueFour ^ xorBit
        bitValueFour = temp
    #print(bitValueFour)
    inOne = '{0:08b}'.format(bitValueFour)
    #print(inOne)

    bitValueFive = bitValueFour << 1
    if(bitValueFive >255):
        temp = bitValueFive ^ removeBitXor
        bitValueFive = temp
        temp = bitValueFive ^ xorBit
        bitValueFive = temp
    #print(bitValueFive)
    inOne = '{0:08b}'.format(bitValueFive)
    #print(inOne)

    bitValueSix = bitValueFive << 1
    if(bitValueSix >255):
        temp = bitValueSix ^ removeBitXor
        bitValueSix = temp
        temp = bitValueSix ^ xorBit
        bitValueSix = temp
    #print(bitValueSix)
    inOne = '{0:08b}'.format(bitValueSix)
    #print(inOne)

    bitValueSeven = bitValueSix << 1
    if(bitValueSeven >255):
        temp = bitValueSeven ^ removeBitXor
        bitValueSeven = temp
        temp = bitValueSeven ^ xorBit
        bitValueSeven = temp
    #print(bitValueSeven)
    inOne = '{0:08b}'.format(bitValueSeven)
    #print(inOne)

    lengthTwo = b.bit_length()
    #print(lengthTwo)
    count = 7
    retValue = 0
    for i in range (lengthTwo):
        if(i == 0):
            bitVal = bitValueZero
        if(i == 1):
            bitVal = bitValueOne
        if(i == 2):
            bitVal = bitValueTwo
        if(i == 3):
            bitVal = bitValueThree
        if(i == 4):
            bitVal = bitValueFour
        if(i == 5):
            bitVal = bitValueFive
        if(i == 6):
            bitVal = bitValueSix
        if(i == 7):
            bitVal = bitValueSeven
            
        if(inTwo[count] == "1"):
            temp = retValue ^ bitVal
            retValue = temp
        count = count - 1

    return retValue
    
def mod(a,b):
    # number = a
    # divisor = b
    while len(bin(a)) >= len(bin(b)):
        lack = len(bin(a)) - len(bin(b))
        a = a ^ (b << lack)
    return a

def multiInverse(a,b):
    # number = a
    # divisor = b = 283 = 1 0001 1011
    if(a == 0) :
        return 0
    for i in range(0,256):
        x = multi(a,i)
        y = mod(x,b)
        if (y == 1):
            return i
        

####
#SBox part start
#SB = "637c777bf26b6fc53001672bfed7ab76ca82c97dfa5947f0add4a2af9ca472c0b7fd9326363ff7cc34a5e5f171d8311504c723c31896059a071280e2eb27b27509832c1a1b6e5aa0523bd6b329e32f8453d100ed20fcb15b6acbbe394a4c58cfd0efaafb434d338545f9027f503c9fa851a3408f929d38f5bcb6da2110fff3d2cd0c13ec5f974417c4a77e3d645d197360814fdc222a908846eeb814de5e0bdbe0323a0a4906245cc2d3ac629195e479e7c8376d8dd54ea96c56f4ea657aae08ba78252e1ca6b4c6e8dd741f4bbd8b8a703eb5664803f60e613557b986c11d9ee1f8981169d98e949b1e87e9ce5528df8ca1890dbfe6426841992d0fb054bb16"
#SBox = bytes.fromhex(SB)
Sbox = []

for i in range(256):
    Sbox.append(i)
divisor = 283    
for i in range(256):
    #Sbox[i] = SBox[i]
    multiInvarseVal = multiInverse(i,divisor)
    #print(multiInvarseVal)
    # convert into 8 bit binary
    multiInvarseVal = format(bin(multiInvarseVal)[2:],'0>8')
    # take reverse order
    multiInvarseVal = multiInvarseVal[::-1]
    b = []
    for j in multiInvarseVal:
        b.append(int(j))

    c = [1,1,0,0,0,1,1,0]
    SBoxTemp = []
    for k in range(8):
        tempSBoxVal = b[k] ^ b[(k+4)%8] ^ b[(k+5)%8] ^ b[(k+6)%8] ^ b[(k+7)%8] ^ c[k]
        SBoxTemp.append(tempSBoxVal)

    sb = ''
    for l in SBoxTemp:
        sb = sb + str(l)
    sb = sb[::-1]
    sbVal = int(sb,2)
    Sbox[i] = sbVal
    #print(SBox[i])
    #print(i,"  :",Sbox[i])

#SBox part complete
####

####
#Key part start
Key = "0f1571c947d9e8590cb7add6af7f6798"
KeyT = "0e1571c947d9e8590cb7add6af7f6798"
#key = input().encode()
#print (Key)
#print (Key[0])

key = bytes.fromhex(Key)
keyT = bytes.fromhex(KeyT)
#print(key)
#print (key[0])

#k = key[0]
#print(k)

#Rcon : '1=01', '2=02', '3=04', '4=08', '5=10', '6=20', '7=40', '8=80', '9=1B', '10=36'.
Rcon = "01000000020000000400000008000000100000002000000040000000800000001B00000036000000"
rcon = bytes.fromhex(Rcon)
#print (rcon[0])

w = []
wT = []
n = 44
m = 4
tempOne = []
tempTwo = []
x = []
y = []
z = []
tempOneT = []
tempTwoT = []
xT = []
yT = []
zT = []

for i in range(m):
    tempOne.append(i)
    tempTwo.append(i)
    x.append(i)
    y.append(i)
    z.append(i)

    tempOneT.append(i)
    tempTwoT.append(i)
    xT.append(i)
    yT.append(i)
    zT.append(i)

for i in range(n):
    w.append([0] * m)
    wT.append([0] * m)

count = 0
for i in range(44):
    if(i <4 ) :
        w[i][0] = key[i*4]
        w[i][1] = key[i*4+1]
        w[i][2] = key[i*4+2]
        w[i][3] = key[i*4+3]

        wT[i][0] = keyT[i*4]
        wT[i][1] = keyT[i*4+1]
        wT[i][2] = keyT[i*4+2]
        wT[i][3] = keyT[i*4+3]
        #print(hex(w[i][0]))
        #print(w[i][1])
        #print(w[i][2])
        #print(w[i][3])
   
    if(i >= 4 ) :
        tempOne[0] = w[i-1][0]
        tempOne[1] = w[i-1][1]
        tempOne[2] = w[i-1][2]
        tempOne[3] = w[i-1][3]

        tempTwo[0] = w[i-4][0]
        tempTwo[1] = w[i-4][1]
        tempTwo[2] = w[i-4][2]
        tempTwo[3] = w[i-4][3]


        tempOneT[0] = wT[i-1][0]
        tempOneT[1] = wT[i-1][1]
        tempOneT[2] = wT[i-1][2]
        tempOneT[3] = wT[i-1][3]

        tempTwoT[0] = wT[i-4][0]
        tempTwoT[1] = wT[i-4][1]
        tempTwoT[2] = wT[i-4][2]
        tempTwoT[3] = wT[i-4][3]

        if(i%4 == 0) :
            x[0] = tempOne[1]
            x[1] = tempOne[2]
            x[2] = tempOne[3]
            x[3] = tempOne[0]

            xT[0] = tempOneT[1]
            xT[1] = tempOneT[2]
            xT[2] = tempOneT[3]
            xT[3] = tempOneT[0]

            y[0] = Sbox[x[0]]
            y[1] = Sbox[x[1]]
            y[2] = Sbox[x[2]]
            y[3] = Sbox[x[3]]

            yT[0] = Sbox[xT[0]]
            yT[1] = Sbox[xT[1]]
            yT[2] = Sbox[xT[2]]
            yT[3] = Sbox[xT[3]]

            #print(y[0])
            #print(y[1])
            #print(y[2])
            #print(y[3])

            z[0] = y[0] ^ rcon[count*4+0]  
            z[1] = y[1] ^ rcon[count*4+1]
            z[2] = y[2] ^ rcon[count*4+2]
            z[3] = y[3] ^ rcon[count*4+3]

            zT[0] = yT[0] ^ rcon[count*4+0]  
            zT[1] = yT[1] ^ rcon[count*4+1]
            zT[2] = yT[2] ^ rcon[count*4+2]
            zT[3] = yT[3] ^ rcon[count*4+3]
            
            count = count + 1

            #print(z[0])
            #print(z[1])
            #print(z[2])
            #print(z[3])

            tempOne[0] = z[0]
            tempOne[1] = z[1]
            tempOne[2] = z[2]
            tempOne[3] = z[3]

            tempOneT[0] = zT[0]
            tempOneT[1] = zT[1]
            tempOneT[2] = zT[2]
            tempOneT[3] = zT[3]

        w[i][0] = tempOne[0] ^ tempTwo[0]
        w[i][1] = tempOne[1] ^ tempTwo[1]
        w[i][2] = tempOne[2] ^ tempTwo[2]
        w[i][3] = tempOne[3] ^ tempTwo[3]

        wT[i][0] = tempOneT[0] ^ tempTwoT[0]
        wT[i][1] = tempOneT[1] ^ tempTwoT[1]
        wT[i][2] = tempOneT[2] ^ tempTwoT[2]
        wT[i][3] = tempOneT[3] ^ tempTwoT[3]
        
        #print(hex(w[i][0]), hex(w[i][1]), hex(w[i][2]), hex(w[i][3]))

#Key part complete
####


# Input and key column wise increasing
####
#Input part start
INPUT = "0123456789abcdeffedcba9876543210"
INPUTtwo = "0123456789abcdeffedcba9876543210"
print("Input One :" + INPUT)
print("Input Two :" + INPUTtwo)

#my_hexdata = INPUT[0]+INPUT[1]
#scale = 16
#num_of_bits = 8
#inone = bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)
#print("Input One in Binary:" + inone)

changeCount = 0
for i in range(16):
    if (INPUT[i] != INPUTtwo[i] ):
        changeCount = changeCount + 1
print("Num of Bytes Differ :",changeCount)


scale = 16
num_of_bits = 8
binaryOne = ""
binaryTwo = ""
for i in range(16):
    tempBinOne = INPUT[i*2]+INPUT[i*2+1]
    tempBinTwo = INPUTtwo[i*2]+INPUTtwo[i*2+1]
    binNumOne = bin(int(tempBinOne, scale))[2:].zfill(num_of_bits)
    binaryOne = binaryOne + binNumOne
    binNumTwo = bin(int(tempBinTwo, scale))[2:].zfill(num_of_bits)
    binaryTwo = binaryTwo + binNumTwo
    
changeCount = 0
for i in range(128):
    if (binaryOne[i] != binaryTwo[i] ):
        changeCount = changeCount + 1
print("Num of Bits Differ :",changeCount)
print("")

Input = bytes.fromhex(INPUT)
InputTwo = bytes.fromhex(INPUTtwo)

tempIn = []
newIn = []
afterSub = []
afterShift = []
afterMix = []
lastTemp = []

tempInTwo = []
newInTwo = []
afterSubTwo = []
afterShiftTwo = []
afterMixTwo = []
lastTempTwo = []

for i in range(16):
    tempIn.append(i)
    newIn.append(i)
    afterSub.append(i)
    afterShift.append(i)
    afterMix.append(i)
    lastTemp.append(i)

    tempInTwo.append(i)
    newInTwo.append(i)
    afterSubTwo.append(i)
    afterShiftTwo.append(i)
    afterMixTwo.append(i)
    lastTempTwo.append(i)
    
for i in range(16):
    tempIn[i] = Input[i]
    tempInTwo[i] = InputTwo[i]
    #print(hex(tempIn[i]))

#print(hex(tempIn[0]), hex(tempIn[4]), hex(tempIn[8]), hex(tempIn[12]))
#print(hex(tempIn[1]), hex(tempIn[5]), hex(tempIn[9]), hex(tempIn[13]))
#print(hex(tempIn[2]), hex(tempIn[6]), hex(tempIn[10]), hex(tempIn[14]))
#print(hex(tempIn[3]), hex(tempIn[7]), hex(tempIn[11]), hex(tempIn[15]))


for i in range(10):
    for j in range(4):
        newIn[j] = tempIn[j] ^ w[i*4+0][j]
        newIn[j+4] = tempIn[j+4] ^ w[i*4+1][j]
        newIn[j+8] = tempIn[j+8] ^ w[i*4+2][j]
        newIn[j+12] = tempIn[j+12] ^ w[i*4+3][j]

        newInTwo[j] = tempInTwo[j] ^ wT[i*4+0][j]
        newInTwo[j+4] = tempInTwo[j+4] ^ wT[i*4+1][j]
        newInTwo[j+8] = tempInTwo[j+8] ^ wT[i*4+2][j]
        newInTwo[j+12] = tempInTwo[j+12] ^ wT[i*4+3][j]
        
        #print(hex(w[i*4+0][j]), hex(w[i*4+1][j]), hex(w[i*4+2][j]), hex(w[i*4+3][j]))
        #print(hex(newIn[j]), hex(newIn[j+4]), hex(newIn[j+8]), hex(newIn[j+12]))
    
    for i in range(16):
        tempIn[i] = newIn[i]
        tempInTwo[i] = newInTwo[i]
    #print(" ")
    #print(hex(newIn[0]), hex(newIn[4]), hex(newIn[8]), hex(newIn[12]))
    #print(hex(newIn[1]), hex(newIn[5]), hex(newIn[9]), hex(newIn[13]))
    #print(hex(newIn[2]), hex(newIn[6]), hex(newIn[10]), hex(newIn[14]))
    #print(hex(newIn[3]), hex(newIn[7]), hex(newIn[11]), hex(newIn[15]))

    cipher = ""
    cipherTwo = ""
    for i in range(16):
        if(newIn[i] <16):
            cipher = cipher+"0"+hex(newIn[i])[2:]
        if(newIn[i] >15):
            cipher = cipher+hex(newIn[i])[2:]
        if(newInTwo[i] <16):
            cipherTwo = cipherTwo+"0"+hex(newInTwo[i])[2:]
        if(newInTwo[i] >15):
            cipherTwo = cipherTwo+hex(newInTwo[i])[2:]
    print(" ")
    print("Cipher One :"+cipher)
    print("Cipher Two :"+cipherTwo)
    changeCount = 0
    for i in range(16):
        if (cipher[i] != cipherTwo[i] ):
            changeCount = changeCount + 1
    print("Num of Bytes Differ :",changeCount)
    
    #bit count start
    scale = 16
    num_of_bits = 8
    binaryOne = ""
    binaryTwo = ""
    for i in range(16):
        tempBinOne = cipher[i*2]+cipher[i*2+1]
        tempBinTwo = cipherTwo[i*2]+cipherTwo[i*2+1]
        binNumOne = bin(int(tempBinOne, scale))[2:].zfill(num_of_bits)
        binaryOne = binaryOne + binNumOne
        binNumTwo = bin(int(tempBinTwo, scale))[2:].zfill(num_of_bits)
        binaryTwo = binaryTwo + binNumTwo
        
    changeCount = 0
    for i in range(128):
        if (binaryOne[i] != binaryTwo[i] ):
            changeCount = changeCount + 1
    print("Num of Bits Differ :",changeCount)
    print("")
    #bit count end
    
    if ( i > 0 ):
        #SUB BYTES
        for j in range(16):
            afterSub[j] = Sbox[tempIn[j]]
            afterSubTwo[j] = Sbox[tempInTwo[j]]
            #print(hex(afterSub[j]))

        for j in range(16):
            tempIn[j] = afterSub[j]
            tempInTwo[j] = afterSubTwo[j]
            #print(hex(tempIn[j]))

        #SHIFT ROW
        afterShift[0] = tempIn[0]
        afterShift[4] = tempIn[4]
        afterShift[8] = tempIn[8]
        afterShift[12] = tempIn[12]

        afterShift[1] = tempIn[5]
        afterShift[5] = tempIn[9]
        afterShift[9] = tempIn[13]
        afterShift[13] = tempIn[1]

        afterShift[2] = tempIn[10]
        afterShift[6] = tempIn[14]
        afterShift[10] = tempIn[2]
        afterShift[14] = tempIn[6]

        afterShift[3] = tempIn[15]
        afterShift[7] = tempIn[3]
        afterShift[11] = tempIn[7]
        afterShift[15] = tempIn[11]


        afterShiftTwo[0] = tempInTwo[0]
        afterShiftTwo[4] = tempInTwo[4]
        afterShiftTwo[8] = tempInTwo[8]
        afterShiftTwo[12] = tempInTwo[12]

        afterShiftTwo[1] = tempInTwo[5]
        afterShiftTwo[5] = tempInTwo[9]
        afterShiftTwo[9] = tempInTwo[13]
        afterShiftTwo[13] = tempInTwo[1]

        afterShiftTwo[2] = tempInTwo[10]
        afterShiftTwo[6] = tempInTwo[14]
        afterShiftTwo[10] = tempInTwo[2]
        afterShiftTwo[14] = tempInTwo[6]

        afterShiftTwo[3] = tempInTwo[15]
        afterShiftTwo[7] = tempInTwo[3]
        afterShiftTwo[11] = tempInTwo[7]
        afterShiftTwo[15] = tempInTwo[11]

        for j in range(16):
            tempIn[j] = afterShift[j]
            lastTemp[j] = afterShift[j]

            tempInTwo[j] = afterShiftTwo[j]
            lastTempTwo[j] = afterShiftTwo[j]
            #print(hex(tempIn[j]))

        #MIX COLUMN
        for j in range(4):
            numOne = multi(tempIn[j*4+0], 2)
            numTwo = multi(tempIn[j*4+1], 3)
            numThree = tempIn[j*4+2]
            numFour = tempIn[j*4+3]      
            num = numOne ^ numTwo ^ numThree ^ numFour
            afterMix[j*4+0] = num
            #print(hex(afterMix[j*4+0]))
            numOne = multi(tempInTwo[j*4+0], 2)
            numTwo = multi(tempInTwo[j*4+1], 3)
            numThree = tempInTwo[j*4+2]
            numFour = tempInTwo[j*4+3]      
            num = numOne ^ numTwo ^ numThree ^ numFour
            afterMixTwo[j*4+0] = num

            numOne = tempIn[j*4+0]
            numTwo = multi(tempIn[j*4+1], 2)
            numThree = multi(tempIn[j*4+2], 3)
            numFour = tempIn[j*4+3]           
            num = numOne ^ numTwo ^ numThree ^ numFour
            afterMix[j*4+1] = num
            #print(hex(afterMix[j*4+1]))
            numOne = tempInTwo[j*4+0]
            numTwo = multi(tempInTwo[j*4+1], 2)
            numThree = multi(tempInTwo[j*4+2], 3)
            numFour = tempInTwo[j*4+3]           
            num = numOne ^ numTwo ^ numThree ^ numFour
            afterMixTwo[j*4+1] = num

            numOne = tempIn[j*4+0]
            numTwo = tempIn[j*4+1]
            numThree = multi(tempIn[j*4+2], 2)
            numFour = multi(tempIn[j*4+3], 3)           
            num = numOne ^ numTwo ^ numThree ^ numFour
            afterMix[j*4+2] = num
            #print(hex(afterMix[j*4+2]))
            numOne = tempInTwo[j*4+0]
            numTwo = tempInTwo[j*4+1]
            numThree = multi(tempInTwo[j*4+2], 2)
            numFour = multi(tempInTwo[j*4+3], 3)           
            num = numOne ^ numTwo ^ numThree ^ numFour
            afterMixTwo[j*4+2] = num

            numOne = multi(tempIn[j*4+0], 3)
            numTwo = tempIn[j*4+1]
            numThree = tempIn[j*4+2]
            numFour = multi(tempIn[j*4+3], 2)           
            num = numOne ^ numTwo ^ numThree ^ numFour
            afterMix[j*4+3] = num
            #print(hex(afterMix[j*4+3]))
            numOne = multi(tempInTwo[j*4+0], 3)
            numTwo = tempInTwo[j*4+1]
            numThree = tempInTwo[j*4+2]
            numFour = multi(tempInTwo[j*4+3], 2)           
            num = numOne ^ numTwo ^ numThree ^ numFour
            afterMixTwo[j*4+3] = num
            
        
        for j in range(16):
            tempIn[j] = afterMix[j]
            tempInTwo[j] = afterMixTwo[j]


for j in range(16):
    tempIn[j] = lastTemp[j]
    tempInTwo[j] = lastTempTwo[j]

#print(hex(tempIn[0]), hex(tempIn[4]), hex(tempIn[8]), hex(tempIn[12]))
#print(hex(tempIn[1]), hex(tempIn[5]), hex(tempIn[9]), hex(tempIn[13]))
#print(hex(tempIn[2]), hex(tempIn[6]), hex(tempIn[10]), hex(tempIn[14]))
#print(hex(tempIn[3]), hex(tempIn[7]), hex(tempIn[11]), hex(tempIn[15]))

#for j in range(4):
#    print(hex(w[40][j]), hex(w[41][j]), hex(w[42][j]), hex(w[43][j]))

for j in range(4):
    newIn[j] = tempIn[j] ^ w[40][j]
    newIn[j+4] = tempIn[j+4] ^ w[41][j]
    newIn[j+8] = tempIn[j+8] ^ w[42][j]
    newIn[j+12] = tempIn[j+12] ^ w[43][j]

    newInTwo[j] = tempInTwo[j] ^ wT[40][j]
    newInTwo[j+4] = tempInTwo[j+4] ^ wT[41][j]
    newInTwo[j+8] = tempInTwo[j+8] ^ wT[42][j]
    newInTwo[j+12] = tempInTwo[j+12] ^ wT[43][j]

#print(" ")
#print(hex(newIn[0]), hex(newIn[4]), hex(newIn[8]), hex(newIn[12]))
#print(hex(newIn[1]), hex(newIn[5]), hex(newIn[9]), hex(newIn[13]))
#print(hex(newIn[2]), hex(newIn[6]), hex(newIn[10]), hex(newIn[14]))
#print(hex(newIn[3]), hex(newIn[7]), hex(newIn[11]), hex(newIn[15]))

cipher = ""
cipherTwo = ""
for i in range(16):
    if(newIn[i] <16):
        cipher = cipher+"0"+hex(newIn[i])[2:]
    if(newIn[i] >15):
        cipher = cipher+hex(newIn[i])[2:]
    if(newInTwo[i] <16):
        cipherTwo = cipherTwo+"0"+hex(newInTwo[i])[2:]
    if(newInTwo[i] >15):
        cipherTwo = cipherTwo+hex(newInTwo[i])[2:]
print(" ")
print("Cipher One :"+cipher)
print("Cipher Two :"+cipherTwo)

changeCount = 0
for i in range(16):
    if (cipher[i] != cipherTwo[i] ):
        changeCount = changeCount + 1
print("Num of Bytes Differ :",changeCount)

scale = 16
num_of_bits = 8
binaryOne = ""
binaryTwo = ""
for i in range(16):
    tempBinOne = cipher[i*2]+cipher[i*2+1]
    tempBinTwo = cipherTwo[i*2]+cipherTwo[i*2+1]
    binNumOne = bin(int(tempBinOne, scale))[2:].zfill(num_of_bits)
    binaryOne = binaryOne + binNumOne
    binNumTwo = bin(int(tempBinTwo, scale))[2:].zfill(num_of_bits)
    binaryTwo = binaryTwo + binNumTwo
    
changeCount = 0
for i in range(128):
    if (binaryOne[i] != binaryTwo[i] ):
        changeCount = changeCount + 1
print("Num of Bits Differ :",changeCount)
print("")

