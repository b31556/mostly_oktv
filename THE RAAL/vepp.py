def inin():
    inpu=input(">")
    if " " in inpu:
        ll=[]
        for l in inpu.split(" "):
            ll.append(int(l))
        return ll
    return int(inpu)
import time
import random

"""
tabla=[]
rows, cols = inin()
for i in range(rows):
    tabla.append(inin())

tabla=[]
rows,cols=224,224
for i in range(224):
    tabla.append([])
    for ii in range(224):
        tabla[i].append(random.randint(0,50) if random.randint(0,1) == 0 else 0)

"""
rows,cols=4,7
tabla=[
    [3,3,0,0,9,0,1],
    [2,5,0,0,0,0,4],
    [0,0,0,5,1,0,3],
    [0,0,0,0,2,4,0]
]

######### calc
import sys

sys.setrecursionlimit(10**6)


starttime=time.time()


now_height=0

groups = {}

def see(x,y,now_height):
    global seen
    if not(-1<x<rows and -1<y<cols):
        return []
    if not (x,y) in seen and tabla[x][y] >= now_height:
        if tabla[x][y] != 0:

            seen.append((x,y))
            
            sord=[(x,y)]

            sord+=see(x+1,y,tabla[x][y])
            sord+=see(x,y+1,tabla[x][y])
            sord+=see(x-1,y,tabla[x][y])
            sord+=see(x,y-1,tabla[x][y])

            return sord

    return []



for x, row in enumerate(tabla):
    for y, height in enumerate(row):
        if height != 0:
            seen = []
            natgeo = see(x,y,height)
            if len(natgeo) != 0:
                
                groups[(x,y)]=natgeo


todel=[]
for ge in groups:
    bigass=True
    natgeo=groups[ge]
    for gg in natgeo:
        if gg in groups:
            if len(groups[gg]) < len(natgeo):
                todel.append(gg)
                
            else:
                bigass=False
        
for t in todel:
    try:
        del groups[t]
    except:
        pass


                    


print(len(groups))





print(f"done in {round(time.time() - starttime,5)}s")
pass