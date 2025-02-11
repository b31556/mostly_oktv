num_houses, num_antenas = input(" > ").split(" ")
houses = input(" > ").split(" ")
antenas = []
for i in range(int(num_antenas)):
    antena = int(input(" > "))
    antenas.append(antena)

for antena in antenas:
    hc = 0
    max_h_m = 0
    for house in houses:
        if int(house) > antena:
            hc += 1
            break
        hc += 1
    print(hc)