import pandas as pd

if __name__ == '__main__':
    gyemantok = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
    # gyémántok adatokat letöltjük

    ##print(diamonds['carat'])
    # csak az oszlop megjelenítése


    #Minta az összegzésre
    sum = 0
    for i in gyemantok['carat']:
        sum += i
    print('karát összesen: ' + str(sum))


    atlag = sum / gyemantok.count()
    print('átlag: ' + str(atlag))



    szum = 0

    for gyemant in gyemantok.iterrows():
        pass
        # ha a gyémánt színe 'H'
        # akkor addjuk össze a price oszolopból az értékeket

    for gyemant in gyemantok.iterrows():
        color = gyemant[1]['color']
        price = gyemant[1]['price']
        if color == 'H':
            szum += price
            # print(gyemant)

    print("Összes ára: " + str(szum))