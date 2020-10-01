##Original puzzle file has 505 phrases
fileHeader = b'\x07\xCF\xAF\x68\x2F\x6C\x20\x72\x65\x63\x6F\x72\x64\x73\x20\x2B\x72\x65\x63\x6C\x65\x6E\x2B\x33\x37\x2B\x32\x20\x42\x59\x54\x45\x53\x00\x00\x00\x00\x00\x00\x00'
fileTail = b'\x0D\x0A' ##also known as \r\n
phraseBegin = b'\x0D\x0A'
phraseSize = 0xAF
MinPhrases = 505
AmPhrases = MinPhrases

## 1 base array ;)
rowSize = [-1,12,14,14,12]
rowOffset = [-1,1,0,0,1]

##bytes(ammounnt of 0x00s you want)

##Function converts string to binary array where spaces are 0x00
def convertString(phrase):
    ##All phrases must be upper case
    phrase = phrase.upper()
    new = b''
    for char in phrase:
        if(char == ' '):
            new += b'\x00'
        else:
            new += bytes([ord(char)])
    return new

## Write FileHeader
#loop
## Write phraseBegin
## Input phrases
#end
##Write fileTail
##flush
newFile = fileHeader

##for i in range(505):
##    newPhrase = phraseBegin
##    newPhrase += convertString("")
##    fillerSize = phraseSize - len(newPhrase)
##    newPhrase += bytes(fillerSize)
##    newFile += newPhrase
##
##newFile += fileTail
##
##file = open("puzzles.bin","wb")
##file.write(newFile)
##file.close()

def createPhrase(phrase,shift=0):
    #Lots of vars
    row = 1
    phrase = phrase.upper()
    sentences = phrase.split()
    new = phraseBegin
    i = 0
    row = 1
    remaining = rowSize[row]
    midrow = False
    looping = True
    while looping:
        word = sentences[i]
        
        newRemaining = (remaining - (len(word)+1))
        
        if(newRemaining <= 0):
            row += 1
            new += bytes(remaining)
            remaining = rowSize[row]

        else:
            i += 1
            new += convertString(word)
            new += b'\x00'
            remaining = newRemaining
            
        if(i >= len(sentences)):
            looping = False

    ## Make sure our phrase is the proper size by filling the rest
    fillerSize = phraseSize - len(new)
    new += bytes(fillerSize)
    return new

##    tst += "............................."
##    print("|@" + tst[0] + tst[1] + tst[2] + tst[3] + tst[4] + tst[5] + tst[6] + tst[7] + tst[8] + tst[9] + tst[10] + tst[11] + "@|")
##    print("|" + tst[12] + tst[13] + tst[14] + tst[15] + tst[16] + tst[17] + tst[18] + tst[19] + tst[20] + tst[21] + tst[22] + tst[23] + tst[24] + tst[25]+ "|")
##    print("|" + tst[26] + tst[27] + tst[28] + tst[29] + tst[30] + tst[31] + tst[32] + tst[33] + tst[34] + tst[35] + tst[36] + tst[37] + tst[38] + tst[39]+ "|")
##    print("|@" + tst[40] + tst[41] + tst[42] + tst[43] + tst[44] + tst[45] + tst[46] + tst[47] + tst[48] + tst[49] + tst[50] + tst[51] + "@|")

##Time for the accual file creation
sfile = open("puzzles.txt","rt")
sentences = sfile.read().split("\n")
sfile.close()
#print(sentences)

puzzleFile = open("puzzles.bin","wb")
puzzleFile.write(fileHeader)

for sentence in sentences:
    AmPhrases -= 1
    puzzleFile.write(createPhrase(sentence))

if(AmPhrases < MinPhrases):
    print("Quota of " + str(MinPhrases) + " not reached. We need " + str(AmPhrases) + " more! Duplicating puzzles")

    for i in range(AmPhrases):
        f = sentences[i%len(sentences)]
        puzzleFile.write(createPhrase(f))

puzzleFile.write(fileTail)
puzzleFile.close()














    
