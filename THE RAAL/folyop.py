import time
import random

def inin():
    inpu=input(">")
    if " " in inpu:
        ll=[]
        for l in inpu.split(" "):
            ll.append(int(l))
        return ll
    return int(inpu)

#hn, money = inin()
#houses = inin()
houses=[]
money=10000000
for i in range(100000):
    houses.append(random.randint(0,10000))

print("started")


# counting 0
starttime=time.time()


results=[]

for pl,ho in enumerate(houses):
    osz_price=ho
    num_houses=1
    for i in range(pl+1,len(houses)):
        if osz_price+houses[i] <= money:
            num_houses+=1
            osz_price+=houses[i]
        else:
            break


    results.append(num_houses)
    

    
print(max(results))







print(f"done in {round(time.time() - starttime,5)}s")