

# Input bilangan dari pengguna
bilangan = int(input("Masukkan bilangan: "))


# Inisialisasi daftar untuk menyimpan faktor-faktor bilangan
faktor = []


# Mencari faktor-faktor bilangan
for i in range(1, bilangan + 1):
    if bilangan % i == 0:
        faktor.append(i)


# Mencetak faktor-faktor bilangan
print("Faktor-faktor 4 dari", bilangan, "adalah:")
for f in faktor:
    print(f)
