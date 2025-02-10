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




def kijut(x,route):
    if x in route:
        return
    route.append(x)
    if x == 1:
        return route
    for i in range(x,1):
        if i in terems[x]:
            return kijut(i,route)
    




print(kijut(5,[]))