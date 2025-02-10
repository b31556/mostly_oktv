while True:

    import json
    route=json.loads(input(" > "))


    aku=0
    max_aku=0
    capacity = 0
    last=route[0]
    for r in route:
        emelkedes = r-last
        aku -= emelkedes
        if aku < 0:
            max_aku += abs(aku)
            aku = 0
        last=r

    aku=max_aku
    last=route[0]
    for r in route:
        emelkedes = r-last
        aku -= emelkedes
        print(f"megyünk {last} ról {r}-ra ez {emelkedes} energia lessz, az akuban ezután {aku} energgia van")
        last=r
        if aku > capacity:
            capacity = aku

    print(max_aku)
    print(capacity)