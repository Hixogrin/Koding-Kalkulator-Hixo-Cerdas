print("hello!")
print("silakan mencoba ^_^")
print("Kalkulator sederhana")
print(15 * "=")

# Memasukkan angka pertama dengan pengecekan kesalahan input
try:
    angka_1 = float(input("masukkan angka pertama: "))
except ValueError:
    print("Mohon masukkan angka yang benar!")
    exit()  # Menghentikan program jika input bukan angka

# Memasukkan operator dan mengecek apakah valid
operator = input("operator (+, -, *, /): ")
if operator not in ["+", "-", "*", "/"]:
    print("Mohon masukkan operator yang benar!")
    exit()  # Menghentikan program jika input operator tidak valid

# Memasukkan angka kedua dengan pengecekan kesalahan input
try:
    angka_2 = float(input("masukkan angka kedua: "))
except ValueError:
    print("Mohon masukkan angka yang benar!")
    exit()  # Menghentikan program jika input bukan angka

# Melakukan perhitungan berdasarkan operator yang dimasukkan
if operator == "+":
    hasil = angka_1 + angka_2
    print(f"maka hasilnya {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"maka hasilnya {hasil}")
elif operator == "*":
    hasil = angka_1 * angka_2
    print(f"maka hasilnya {hasil}")
elif operator == "/":
    if angka_2 != 0:  # Memastikan tidak ada pembagian dengan nol
        hasil = angka_1 / angka_2
        print(f"maka hasilnya {hasil}")
    else:
        print("Pembagian dengan nol tidak diperbolehkan!")

print("akhir dari program, terima kasih telah mencoba!")