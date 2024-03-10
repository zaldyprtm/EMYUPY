import main

# Membuat dictionary untuk menyimpan daftar barang dan harganya
daftar_barang = {
    "Apel": 5000,
    "Jeruk": 7000,
    "Mangga": 10000,
    "Pisang": 4000,
    "Anggur": 12000
}

def hitung_total_pembelian(pembelian):
    total = 0
    for barang, jumlah in pembelian.items():
        harga = daftar_barang.get(barang)
        if harga:
            total += harga * jumlah
    return total

def cetak_struk_pembelian(pembelian, total_pembelian):
    print("\n===== Struk Pembelian =====")
    for barang, jumlah in pembelian.items():
        harga = daftar_barang.get(barang)
        print(f"{barang} \t x{jumlah} \t Rp {harga*jumlah}")
    print("===========================")
    print(f"Total Pembelian \t Rp {total_pembelian}")
    print("===========================")

def kasir():
    pembelian = {}
    while True:
        print("\nDaftar Barang:")
        for barang, harga in daftar_barang.items():
            print(f"{barang}: Rp {harga}")

        barang = input("\nPilih barang yang akan dibeli (ketik 'selesai' untuk menyelesaikan pembelian): ")
        if barang.lower() == 'selesai':
            break

        if barang in daftar_barang:
            jumlah = int(input("Masukkan jumlah barang yang akan dibeli: "))
            pembelian[barang] = pembelian.get(barang, 0) + jumlah
        else:
            print("Barang tidak ditemukan.")

    total_pembelian = hitung_total_pembelian(pembelian)
    cetak_struk_pembelian(pembelian, total_pembelian)

if __name__ == "__main__":
    kasir()
