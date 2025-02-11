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
"""
hn, money = inin()
houses = inin()
"""
houses=[]
money=10000000
for i in range(100000):
    houses.append(random.randint(1,10000))

print("started")


# counting 0
starttime=time.time()


max_selected=0

selected=[]
oszprice=0

for pl,ho in enumerate(houses):
    if oszprice + ho <= money:
        oszprice+=ho
        selected.append(ho)
        
    else:
        while oszprice + ho > money:
            if len(selected) == 0:
                break
            oszprice-=selected.pop(0)
    
        if oszprice + ho <= money:
            oszprice+=ho
            selected.append(ho)
        


    if len(selected) > max_selected:
        max_selected=len(selected)
    

    
print(max_selected)  







print(f"done in {round(time.time() - starttime,5)}s")