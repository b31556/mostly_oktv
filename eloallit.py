terems = {
    1: [3, 4, 5],
    2: [3, 4, 8],
    3: [1, 2, 8],
    4: [1, 2, 6],
    5: [1, 6],
    6: [4, 5, 7],
    7: [6],
    8: [2, 3]
}

posible_paths=[]

def expo(terem,searchfor,routee):
    if terem in routee:
        return
    routee.append(terem)
    if terem == searchfor:
        return routee
    
    for near in terems[terem]:
        ret=expo(near,searchfor,routee)
        if ret:
            return ret


def route(fro,to):
    route=[fro]
    for near in terems[fro]:
        ret=expo(near,to,route)
        if ret:
            final=route
            final.append(near)
            posible_paths.append(final)
    return posible_paths
while True:

    fro = int(input("from > "))
    to = int(input("to > "))

    print(route(fro,to))
