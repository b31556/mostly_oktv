def inin():
    inpu=input(">")
    if " " in inpu:
        ll=[]
        for l in inpu.split(" "):
            ll.append(int(l))
        return ll
    return int(inpu)

noe = inin()
nums=inin()

for i in range(len(nums)):
    for ii in range(i):
        for 