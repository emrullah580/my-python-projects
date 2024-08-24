islem = input("1-Toplama", "2-Çikarma", "3-Çarpma", "4-Bölme")
sa1 = int(input("Birinci sayiyi giriniz: "))
sa2 = int(input("İkinci sayiyi giriniz: "))

def calculator(sayi1, sayi2, islem):
    if islem=="1":
        print(sayi1+sayi2)
        
    elif islem=="2":
        print(sayi1-sayi2)
        
    elif islem=="3":
        print(sayi1*sayi2)
        
    elif islem=="4":
        print(sayi1/sayi2)
        
    else:
        print("Geçersiz")   
        
calculator()