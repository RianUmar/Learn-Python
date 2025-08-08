print("Tugas Konversi Suhu")

# Fahrenheit ke kelvin
suhu_fahrenheit = float(input("Masukan suhu dalam fahrenheit : "))
fahrenheit_kelvin = 5/9 * (suhu_fahrenheit - 32) + 273.15
print ("Suhu dalam kelvin adalah ", fahrenheit_kelvin)

suhu_kelvin = float(input("Masukan suhu dalam kelvin : "))
kelvin_fahrenheit = 9/5 * (suhu_kelvin - 273.15) + 32
print ("Suhu dalam fahrenheit adalah ", kelvin_fahrenheit)