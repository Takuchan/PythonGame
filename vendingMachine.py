def change(price,deposit,available_currency):
    resultdict = {}
    amari = deposit - price
    for a in available_currency:
        while amari - a >= 0:
            if a in resultdict:
                resultdict[a] +=1
            else:
                resultdict[a] = 1
            amari -= a
    return resultdict