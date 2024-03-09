# Program Warung Sederhana
import main
# Inisialisasi variabel untuk menyimpan stok makanan
stok_makanan = {
    "nasi goreng": 10,
    "mie goreng": 10,
    "ayam goreng": 10,
    "soto ayam": 10,
    "gado-gado": 10
}

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("Menu Warung Sederhana:")
    for makanan, stok in stok_makanan.items():
        print(f"{makanan.capitalize()}: Rp 10.000 - Stok: {stok}")

# Fungsi untuk memesan makanan
def pesan_makanan(makanan):
    if makanan.lower() in stok_makanan and stok_makanan[makanan.lower()] > 0:
        print(f"Anda telah memesan {makanan}. Silakan tunggu sebentar!")
        stok_makanan[makanan.lower()] -= 1
        print("Pesanan Anda sedang diproses...")
        print("Terima kasih telah memesan!")
    else:
        print("Maaf, makanan yang Anda pesan tidak tersedia saat ini.")

# Main program
def mulai():
    print("Selamat datang di Warung Sederhana!")
    while True:
        print("\nSilakan pilih menu:")
        print("1. Lihat Menu")
        print("2. Pesan Makanan")
        print("3. Keluar")
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            tampilkan_menu()
        elif pilihan == "2":
            makanan = input("Masukkan makanan yang ingin Anda pesan: ")
            pesan_makanan(makanan)
        elif pilihan == "3":
            print("Terima kasih telah mengunjungi Warung Sederhana!")
            main.main()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")



if __name__ == "__main__":
    mulai()
