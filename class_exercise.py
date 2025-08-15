# class Siswa:
#     def __init__(self, nama, umur, jurusan):
#         self.nama = nama
#         self.umur = umur
#         self.jurusan = jurusan

#     def perkenalan(self):
#         return f"Perkenalkan, Namaku {self.nama} dan umurku {self.umur} dari jurusan {self.jurusan}"


# Siswa1 = Siswa("Ryan", 17, "PPLG")
# Siswa2 = Siswa("Yogi", 17, "BCF")

# print(Siswa1.perkenalan())
# print(Siswa2.perkenalan())


# class Buku:
#     def __init__(self, judul, penulis, stok):
#         self.judul = judul
#         self.penulis = penulis
#         self.stok = stok

#     def info_buku(self):
#         return f"Judul: {self.judul}\nPenulis: {self.penulis}\nStok: {self.stok}"

#     def pinjam(self):
#         if self.stok >= 1:
#             self.stok -= 1
#             print("Buku berhasil dipinjam, Jangan lupa balikin ya!")
#         else:
#             print("Maaf, stok buku sedang habis")

#     def kembalikan(self):
#         self.stok += 1
#         print("Terima kasih sudah mengembalikan")


# buku1 = Buku("Laskar Pelangi", "Andrea Hirata", 3)
# print(buku1.info_buku())

# buku1.pinjam()
# print(buku1.info_buku())

# buku1.kembalikan()
# print(buku1.info_buku())


class Produk:
    toko = "Toko Serba Ada"

    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def info_produk(self):
        return f"Toko : {self.toko}\nProduk : {self.nama}\nHarga : {self.harga}\nStok : {self.stok}"

    def beli(self, jumlah):
        if self.stok >= jumlah:
            total = self.harga * jumlah
            self.stok -= jumlah
            return f"Berhasil membeli {jumlah} {self.nama}, total harga: {total}"
        elif jumlah <= 0:
            return "Jumlah pembelian tidak valid"
        else:
            return f"Maaf, stok tersisa {self.stok}"

    def restok(self, jumlah):
        if self.stok == 0:
            self.stok += jumlah
            return f"Restok berhasil, stok saat ini : {self.stok}"
        else:
            return f"Stok masih tersisa {self.stok}"


produk1 = Produk("Indomie", 5000, 10)
produk2 = Produk("CocaCola", 8000, 10)

print(produk1.info_produk())
print(produk2.info_produk())

print(produk1.beli(5))
print(produk1.beli(5))

print(produk1.info_produk())

print(produk1.restok(6))

print(produk1.info_produk())
