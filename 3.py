belanja_string = input("Total belanja anda : Rp ")
belanja = float(belanja_string)
bayar = belanja

if belanja > 100000 :
    print("Kamu mendapatkan diskon 10%")
    diskon = belanja * 10/100
    bayar = belanja - diskon
else :
    print("Anda tidak mendapatkan diskon")

print(f"total belanja anda : Rp. {bayar}")
