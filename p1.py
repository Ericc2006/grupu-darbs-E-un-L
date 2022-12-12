def sienuaprekinasana():
    siengar = float(input("Ievadi sienas garumu m - "))
    sienplat = float(input("Ievadi sienas  platumu m - "))
    sienaug = float(input("Ievadi sienas augstumu m - "))
    return (siengar * sienaug) * 2 + (sienplat * sienaug) * 2

def gridapr():
    gridgar = float(input("Ievadi grīdas garumu m - "))
    gridplat = float(input("Ievadi grīdas  platumu m - "))
    return gridgar * gridplat

def sienaprekinashana(x):
    if x == 1:
        print("Ievadi 1 istabas sienu izmerus")
        return sienuaprekinasana()
    elif x == 2:
        print("Ievadi 1 istabas sienu izmerus")
        x = sienuaprekinasana()
        print("Ievadi 2 istabas sienu izmerus")
        return  x + sienuaprekinasana()
    elif x == 3:
        print("Ievadi 1 istabas sienu izmerus")
        x = sienuaprekinasana()
        print("Ievadi 2 istabas sienu izmerus")
        c = sienuaprekinasana()
        print("Ievadi 3 istabas sienu izmerus")
        return  x + c + sienuaprekinasana()
    elif x == 4:
        print("Ievadi 1 istabas sienu izmerus")
        x = sienuaprekinasana()
        print("Ievadi 2 istabas sienu izmerus")
        c = sienuaprekinasana()
        print("Ievadi 3 istabas sienu izmerus")
        b = sienuaprekinasana()
        print("Ievadi 4 istabas sienu izmerus")
        return  x + c + b + sienuaprekinasana()

def error(x, kļūdas_nr):
    if x <= 0:
        print("ERORR " + kļūdas_nr)
        print(""""
            001 - iegūts nereāls rezultāts(durvju/logu laukums ir lielāks nekā sienu kopējais laukums)
            002 - ievadīto skaitļu kopsumma ir mazāka vai vienāda ar 0
            003 - skaitlis ir mazāks vai vienāds ar 0
            """)
        exit()