import random

def DO_MAFIC(word):
    
    word=word+"§"

    lit=[]

    for i in range(len(word)):
        mw = word
        for r in range(i):
            mw = mw[-1] + mw[0:len(word)-1]
        lit.append(mw)



    lit.sort()

    nw=""
    for eed in lit:
        nw += eed[-1]

    return nw

    #print(nw)
    #print(lit)





eee=[]
word = "DFASAD"
for ee in word:
    eee.append(ee)

letr=[]


while True:
    random.shuffle(eee)
    wede=""
    for olkok in eee:
        wede+=olkok
    


    d=DO_MAFIC(wede)
    if d=="D§FASAD":
        print(wede)
        break



