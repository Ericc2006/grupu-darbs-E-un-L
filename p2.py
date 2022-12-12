def loguundurvjizm():
    loguaug = float(input("Ievadi loga augstumu m - "))
    loguplat = float(input("Ievadi loga platumu m - "))
    durvjuaug = float(input("Ievadi durvju augstumu m - "))
    durvjuplat = float(input("Ievadi durvju platumu m - "))
    return durvjuplat * durvjuaug + loguaug * loguplat

def durvjuizm():
    durvjuaug = float(input("Ievadi durvju augstumu m - "))
    durvjuplat = float(input("Ievadi durvju platumu m - "))
    return durvjuplat * durvjuaug

def aprekinashana(x, vaiirvainav, vaiirvainav2,vaiirvainav3,vaiirvainav4):
    if x == 1:
        if vaiirvainav == 1:
            print("Ievadi 1 istabas logu un durvju izmerus")
            return loguundurvjizm()
        elif vaiirvainav == 2:
            print("Ievadi 1 istabas durvju izmerus")
            return durvjuizm()
    elif x == 2:
        if vaiirvainav == 1:
            print("Ievadi 1 istabas logu un durvju izmerus")
            c = loguundurvjizm()
            g = 0
        elif vaiirvainav == 2:
            print("Ievadi 1 istabas durvju izmerus")
            g = durvjuizm()
            c = 0
        if vaiirvainav2 == 1:
            print("Ievadi 2 istabas logu un durvju izmerus")
            b = loguundurvjizm()
            return c+g+b
        elif vaiirvainav2 == 2:
            print("Ievadi 2 istabas durvju izmerus")
            d = durvjuizm()
            return c+g+d
    elif x == 3:
        if vaiirvainav == 1:
            print("Ievadi 1 istabas logu un durvju izmerus")
            c = loguundurvjizm()
            g = 0
        elif vaiirvainav == 2:
            print("Ievadi 1 istabas durvju izmerus")
            g = durvjuizm()
            c = 0
        if vaiirvainav2 == 1:
            print("Ievadi 2 istabas logu un durvju izmerus")
            d = loguundurvjizm()
            o = 0
        elif vaiirvainav2 == 2:
            print("Ievadi 2 istabas durvju izmerus")
            o = durvjuizm()
            d = 0
        if vaiirvainav3 == 1:
            print("Ievadi 3 istabas logu un durvju izmerus")
            b = loguundurvjizm()
            return c+g+d+o+b
        elif vaiirvainav3 == 2:
            print("Ievadi 3 istabas durvju izmerus")
            z = durvjuizm()
            return c+g+d+o+z
    elif x == 4:
        if vaiirvainav == 1:
            print("Ievadi 1 istabas logu un durvju izmerus")
            c = loguundurvjizm()
            g = 0
        elif vaiirvainav == 2:
            print("Ievadi 1 istabas durvju izmerus")
            g = durvjuizm()
            c = 0
        if vaiirvainav2 == 1:
            print("Ievadi 2 istabas logu un durvju izmerus")
            d = loguundurvjizm()
            o = 0
        elif vaiirvainav2 == 2:
            print("Ievadi 2 istabas durvju izmerus")
            o = durvjuizm()
            d = 0
        if vaiirvainav3 == 1:
            print("Ievadi 3 istabas logu un durvju izmerus")
            b = loguundurvjizm()
            z = 0
        elif vaiirvainav3 == 2:
            print("Ievadi 3 istabas durvju izmerus")
            z = durvjuizm()
            b = 0
        if vaiirvainav4 == 1:
            print("Ievadi 4 istabas logu un durvju izmerus")
            z1 = loguundurvjizm()
            return c+g+d+o+b+z+z1
        elif vaiirvainav4 == 2:
            print("Ievadi 4 istabas durvju izmerus")
            v = durvjuizm()
            return c+g+d+o+b+z+v
