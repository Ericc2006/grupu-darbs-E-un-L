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

def gridaprekinashana(x):
    if x == 1:
        print("Ievadi 1 istabas grīdas izmerus")
        return gridapr()
    elif x == 2:
        print("Ievadi 1 istabas grīdas izmerus")
        x = gridapr()
        print("Ievadi 2 istabas grīdas izmerus")
        return  x + gridapr()
    elif x == 3:
        print("Ievadi 1 istabas grīdas izmerus")
        x = gridapr()
        print("Ievadi 2 istabas grīdas izmerus")
        c = gridapr()
        print("Ievadi 3 istabas grīdas izmerus")
        return  x + c + gridapr()
    elif x == 4:
        print("Ievadi 1 istabas grīdas izmerus")
        x = gridapr()
        print("Ievadi 2 istabas grīdas izmerus")
        c = gridapr()
        print("Ievadi 3 istabas grīdas izmerus")
        b = gridapr()
        print("Ievadi 4 istabas grīdas izmerus")
        return  x + c + b + gridapr()

def aprekinavisu(x,s,kopistizm,d,price,price1,price2,price3,price4,price5,price6):
    if x == 1:
        if s[0] == 1:
            if kopistizm > s[3]:
                paliek = kopistizm - s[3]
                print(f"Vēl vajag nopirkt {paliek} m2 viniltapetes krāsojamās, kas iznāks {paliek * price6} eiro")
            elif kopistizm == s[3]:
                print(f"Viniltapešu pietiek")
            else:
                print("Viniltapešu ir par daudz")
        elif s[0] == 2:
            if d > s[3]:
                paliek = kopistizm - s[3]
                print(f"Vēl vajag nopirkt {paliek} m2 papīra tapešu, kas iznāks {paliek * price5} eiro")
            elif d == s[3]:
                print(f"Papīra tapešu pietiek")
            else:
                print("Papīratapešu ir par daudz")
        if s[1] == 1:
            if d > s[4]:
                paliek = d - s[4]
                print(f"Vēl vajag nopirkt {paliek} m2 griestuplākšņu, kas iznāks {paliek * price4} eiro")
            elif kopistizm == s[4]:
                print(f"Griestplākšņu pietiek")
            else:
                print("Griestplākšņu ir par daudz")
        elif s[1] == 2:
            None
        if s[2] == 1:
            if d > s[5]:
                paliek = d - s[5]
                print(f"Vēl vajag nopirkt {paliek} m2 ūdensturošo laminātu, kas iznāks {paliek * price} eiro")
            elif d == s[5]:
                print(f"Ūdensturošo lamināta pietiek")
            else:
                print("Ūdensturošo lamināta ir par daudz")
        elif s[2] == 2:
            if d > s[5]:
                paliek = d - s[5]
                print(f"Vēl vajag nopirkt {paliek} m2 lamināta, kas iznāks {paliek * price1} eiro")
            elif kopistizm == s[6]:
                print(f"Lamināta pietiek")
            else:
                print("Lamināta ir par daudz")
        elif s[2] == 3:
            if d > s[5]:
                paliek = d - s[5]
                print(f"Vēl vajag nopirkt {paliek} m2 linoleja, kas iznāks {paliek * price2} eiro")
            elif d == s[5]:
                print(f"Linoleja pietiek")
            else:
                print("Linoleja ir par daudz")
        elif s[2] == 4:
            if d > s[5]:
                paliek = d - s[5]
                print(f"Vēl vajag nopirkt {paliek} m2 grīdas flīžu, kas iznāks {paliek * price3} eiro")
            elif d == s[5]:
                print(f"Grīdas flīžu pietiek")
            else:
                print("Grīdas flīžu ir par daudz")
    elif x == 2:#Nav nopirktu materialu
        if s[0] == 1:
            print(f"Vajag nopirkt {kopistizm} m2 viniltapetes krāsojamās, kas iznāks {kopistizm * price6} eiro")
        elif s[0] == 2:
            print(f"Vajag nopirkt {kopistizm} m2 papīra tapešu, kas iznāks {kopistizm * price5} eiro")
        if s[1] == 1:
            print(f"Vajag nopirkt {d} m2 griestuplākšņu, kas iznāks {d * price4} eiro")
        elif s[1] == 2:
            None
        if s[2] == 1:
            print(f"Vajag nopirkt {d} m2 ūdensturošo laminātu, kas iznāks {d * price} eiro")
        elif s[2] == 2:
            print(f"Vajag nopirkt {d} m2 lamināta, kas iznāks {d * price1} eiro")
        elif s[2] == 3:
            print(f"Vajag nopirkt {d} m2 linoleja, kas iznāks {d * price2} eiro")
        elif s[2] == 4:
            print(f"Vajag nopirkt {d} m2 grīdas flīžu, kas iznāks {d * price3} eiro")