
def calculator():
    while True:
        sa1 = int(input("Birinci sayiyi giriniz: "))
        sa2 = int(input("İkinci sayiyi giriniz: "))
        print("İşlem seçiniz: ")
        print("1- Toplama")
        print("2- Çikarma")
        print("3- Çarpma")
        print("4- Bölme")
        print("exit")
        liste = input("1, 2, 3, 4 veya exit ")
        
        if liste.lower()=="exit":
            break
    
        if liste=="1":
           print(sa1 + sa2) 
           
        elif liste=="2":
            print(sa1 - sa2)
            
        elif liste=="3":
            print(sa1 * sa2)
            
        elif liste=="4":
            if sa2==0:
                print("Hata!")
                
            else:
                print(sa1 / sa2)
                
calculator()
            
        
