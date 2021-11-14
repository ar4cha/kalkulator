
#Varbutibu kalkulators
# Autors: Artjoms Kasperovics
# Datums: 03.11.2021 V2V
import math
def statistiska():

    burtum = int(input("\033[95m notikumu skaits:"))
    burtuk = int(input("eksperimentu skaits:"))

    w = burtum/burtuk;

    if burtum < 0:
        print("\033[93mJusu pirmais skailtlis nevar but negativs, meginiet velreiz")
        statistiska()


    print("\033[1;34;40m statistiskā varbūtība =" + format( w, ",.2f"))
    procent = w*100
    print("Tas bus " + format(procent,",.2f")+"%"+" statistiskā varbūtība")


def geometriksa():

    radius = int(input("\033[95mKada radius un tilpumi:"))
    malas = int(input("kada malas garumu:"))
    π = math.pi

    kvadrats= (math.pow(malas, 2)) / ((math.pow(radius, 2))) * π

    procents = kvadrats*100

    print("\033[1;97;40mvarbūtība ir " + format( procents, ",.2f")+"%")
    if procents>100:
        print("\033[1;31;40mVarbūtība nekad nevar pārsniegt skaitli 1 (jeb 100%)")

def klasiska():
    labveligo = int(input("\033[93mlabvēlīgo notikumu skaits:"))
    notikumu = int (input("visu notikumu kopskaits:"))

    klasika = labveligo/notikumu
    procent2 = klasika*100

    print("\033[1;97;40mvarbūtība ir = " + format( procent2, ",.2f")+'%')


if __name__ == '__main__':
        choice = input("\033[97m Kada veida varbutibas aprekini Tev sodien padoma? \n"
                   "\033[97m Ievadi burtu:\n"
                    "\033[95m-K klasiska metode n no n\n"
                   "\033[96m-G geometriksa varbutiba\n"
                   "\033[92m-S statiska varbutiba k m reizes\n")
        if choice.lower() == 'k':
            klasiska()
        if choice.lower() == 'g':
            geometriksa()
        if choice.lower() == 's':
            statistiska()
        else:
            exit(0)