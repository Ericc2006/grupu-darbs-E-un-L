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

g = p2.aprekinashana(x, vaiirvainav,vaiirvainav2,vaiirvainav3,vaiirvainav4)
kopistizm = c - g
p1.error(g, "002")
p1.error(c, "002")
p1.error(d, "002")
p1.error(kopistizm, "001")

irnav = int(input("""
        Vai jau ir iepirkti vajadzīgie materiāli
        1 - Jā
        2 - Nē
        """))

s = p2.materiali(irnav)
p1.aprekinavisu(x,s,kopistizm,d,price,price1,price2,price3,price4,price5,price6)

# print(g)
# print(c)
# print(d)
# print(s[0])


# p1.istabu()