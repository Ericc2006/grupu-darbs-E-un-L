import p1
import p2

price = 19.95 #ūdensdrošs lamināts
price1 = 8.96 #lamināts
price2 = 9.15 #linolejs
price3 = 12.95 # grīdas flīzes
price4 = 19.99 # griestuplāksnes
price5 = 3.20 # papīra tapetes
price6 = 0.82 # Viniltapetes krāsojamās

x = int(input("Ievadi istabu skaitu - "))
p1.error(x, "003")

c = p1.sienaprekinashana(x)
d = p1.gridaprekinashana(x)

if x == 1:
    vaiirvainav = int(input("""Vai 1 istabā atrodas :
                                    1 - Logs un Durvis
                                    2- Tikai Durvis
                                    """))
    vaiirvainav2 = 0
    vaiirvainav3 = 0
    vaiirvainav4 = 0
elif x == 2:
    vaiirvainav = int(input("""Vai 1 istabā atrodas :
                                    1 - Logs un Durvis
                                    2- Tikai Durvis
                                    """))
    vaiirvainav2 = int(input("""Vai 2 istabā atrodas :
                                    1 - Logs un Durvis
                                    2- Tikai Durvis
                                    """))
    vaiirvainav3 = 0
    vaiirvainav4 = 0
elif x == 3:
    vaiirvainav = int(input("""Vai 1 istabā atrodas :
                                    1 - Logs un Durvis
                                    2- Tikai Durvis
                                    """))
    vaiirvainav2 = int(input("""Vai 2 istabā atrodas :
                                    1 - Logs un Durvis
                                    2- Tikai Durvis
                                    """))
    vaiirvainav3 = int(input("""Vai 3 istabā atrodas :
                                    1 - Logs un Durvis
                                    2- Tikai Durvis
                                    """))
    vaiirvainav4 = 0
elif x == 4:
    vaiirvainav = int(input("""Vai 1 istabā atrodas :
                                    1 - Logs un Durvis
                                    2- Tikai Durvis
                                    """))
    vaiirvainav2 = int(input("""Vai 2 istabā atrodas :
                                    1 - Logs un Durvis
                                    2- Tikai Durvis
                                    """))
    vaiirvainav3 = int(input("""Vai 3 istabā atrodas :
                                    1 - Logs un Durvis
                                    2- Tikai Durvis
                                    """))
    vaiirvainav4 = int(input("""Vai 4 istabā atrodas :
                                    1 - Logs un Durvis
                                    2- Tikai Durvis
                                    """))
