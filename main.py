#---------------------------INPUT FUNCTIONS--------------------------- 

#---------------------------TOTAL TEST NUMBER---------------------------
def main(totaltest, toplamsayi, syc, islem, usrsayi, depo): 
    totaltest = 0
    syc = -1 #reset counter
    depo = "" #reset depo
    totaltest = int(input())
    
    if totaltest < 0 or totaltest > 100: 
          r_main(totaltest, toplamsayi, syc, islem, usrsayi, depo)
          return
    else:
            f_toplamsayi(totaltest, usrsayi, islem, toplamsayi, syc, depo)
            return   

#---------------------------TEST LENGTH NUMBER---------------------------     
def f_toplamsayi(totaltest, usrsayi, islem, toplamsayi, syc, depo):
    
    syc += 1
    if syc < totaltest:
            toplamsayi = 0
            toplamsayi = int(input())
            if toplamsayi <= 0 or toplamsayi > 100:
                r_main(totaltest, toplamsayi, syc, islem, usrsayi, depo)
                return
            elif toplamsayi > 0 and toplamsayi <= 100:
                f_usrsayi(totaltest, toplamsayi, islem, usrsayi, syc, depo)    
                return  
            return
    elif syc == totaltest:
         print(*depo.split(), sep="\n")
         r_main(totaltest, toplamsayi, syc, islem, usrsayi, depo)
    return toplamsayi, syc, totaltest

#---------------------------USER INPUT NUMBERS---------------------------
def f_usrsayi(totaltest, toplamsayi, islem, usrsayi, syc, depo):
     
     if syc < totaltest:
            usrsayi = 0
            usrsayi = input()
            islem = sum(map(calc, usrsayi.split()))          
            if len(usrsayi.split()) != toplamsayi:
                depo = depo + " " + str(-1)
                r_toplamsayi(totaltest, usrsayi, islem, toplamsayi, syc, depo)
                return 
            else:
                depo = depo + " " + str(islem)
                f_toplamsayi(totaltest, usrsayi, islem, toplamsayi, syc, depo)
     return usrsayi, toplamsayi, syc, totaltest, islem, depo

#---------------------------CALCULATION---------------------------
def calc(usrsayi):
    isayisi = int(usrsayi)
    if isayisi < 0:
        return isayisi ** 4
    elif isayisi >= 0:
        isayisi = 0
        return isayisi
    return isayisi

#---------------------------RETURN FUNCTIONS---------------------------
def r_main(totaltest, toplamsayi, syc, islem, usrsayi, depo):
    main(totaltest, toplamsayi, syc, islem, usrsayi, depo)
    return

def r_toplamsayi(totaltest, usrsayi, islem, toplamsayi, syc, depo):
    f_toplamsayi(totaltest, usrsayi, islem, toplamsayi, syc, depo)
    return

#---------------------------START---------------------------
if __name__ == "__main__":
    totaltest = 0
    toplamsayi = 0
    usrsayi = 0
    islem = str
    syc = 0
    depo = ""
    main(totaltest, toplamsayi, syc, islem, usrsayi, depo)
    
    