balans = 1000 
print("emeliyyat kodlari: ") 
print("1 - balansa bax") 
print("2 - pul cixar") 
print("3 - pul yatir") 
print("0 - cixis") 
emeliyyat = int(input("emeliyyat kodunu girin: "))  
while balans > 0: 
    match emeliyyat: 
        case 1: 
            print(balans) 
            break
        case 2: 
            miqdar = int(input("cixilan pulun meblegi? ")) 
            if balans > miqdar: 
                balans = balans - miqdar 
                print(balans) 
                break
            else: 
                print("balans kifayet deyil") 
                break
        case 3: 
            miqdar = int(input("daxil olunan pulun meblegi? ")) 
            balans = balans + miqdar 
            print(balans) 
            break
        case 0:  
            break