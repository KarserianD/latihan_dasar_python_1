# Tantangan 1 Operator Dasar ==============================
input_pertama = int(input("Masukin Angka Pertama : "))
input_kedua = int(input("Masukin Angka Kedua : "))

penjumlahan = input_pertama + input_kedua
pengurangan = input_pertama - input_kedua
perkalian = input_pertama * input_kedua
if input_kedua != 0:
    pembagian = round(input_pertama / input_kedua, 2)
    sisa_bagi = input_pertama % input_kedua
else:
    pembagian = "Tidak bisa dibagi nol!"
    sisa_bagi = "Tidak bisa dibagi nol!"

print(f"{input_pertama} + {input_kedua} = {penjumlahan}")
print(f"{input_pertama} - {input_kedua} = {pengurangan}")
print(f"{input_pertama} * {input_kedua} = {perkalian}")
print(f"{input_pertama} / {input_kedua} = {pembagian}")
print(f"{input_pertama} % {input_kedua} = {sisa_bagi}")


# Tantangan 2 Operator Perbandingan & Logika ==============
umur = input("Berapa umur kamu? : ")

if umur.isdigit():
    umur = int(umur)
    status_sim = input("Udah punya SIM? (punya/belum) : ").strip().lower()

    if umur >= 17 and status_sim == ("punya"):
        print("Boleh mengemudi")
    elif umur >= 17 and status_sim == ("belum"):
        print("Harus buat SIM dulu")
    else:
        print("Belum boleh mengemudi")
else:
    print("ketik Angka Umur Kamu!")


# Tantangan 3 Conditional Statement =======================
nilai = input("Nilai ujian kamu : ")

if nilai.isdigit():
    nilai = int(nilai)

    if nilai >= 90:
        print("Nilai A")
    elif nilai >= 75:
        print("Nilai B")
    elif nilai >= 60:
        print("Nilai C")
    else:
        print("Tidak Lulus")
else:
    print("Masukkan angka!")


# Tantangan 4 Mini Project : Calculator Diskon ============
harga_barang = input("Masukkan Harga Barang : ")

if harga_barang.isdigit():
    harga_barang = int(harga_barang)
    kode_promo = input("Masukkan kode promo : ").upper()

    if kode_promo == ("HEMAT10"):
        total_harga = harga_barang - (10 / 100 * harga_barang)
        print(f"""Berhasil menggunakan kode promo!
                Total harga : {harga_barang} + Diskon 10%
                Total Keseluruhan : {round(total_harga)}""")
    elif kode_promo == ("HEMAT20"):
        total_harga = harga_barang - (20 / 100 * harga_barang)
        print(f"""Berhasil menggunakan kode promo!
                Total harga : {harga_barang} + Diskon 20%
                Total keseluruhan : {round(total_harga)}""")
    else:
        print(f"""Kode Promo tidak valid!
                Total harga : {harga_barang}""")
else:
    print("Masukkan nominal barang!")
