

def calculator():
    print("İşlem seçin ")
    print("1-Toplama", "2-Çikarma", "3-Çarpma", "4-Bölme")
    
    islem = input("Seçim Yapin[1-2-3-4]")
    sa1 = int(input("Birinci sayiyi giriniz: "))
    sa2 = int(input("İkinci sayiyi giriniz: "))
    
    if islem=="1":
        print(sa1 + sa2)
        
    elif islem=="2":
        print(sa1 - sa2)
        
    elif islem=="3":
        print(sa1 * sa2)
        
    elif islem=="4":
        print(sa1 / sa2)
        
    else:
        print("Geçersiz")   
        
calculator()