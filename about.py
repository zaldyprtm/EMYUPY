

def utama():
    print('\nSelamat datang di Program MuzalPra untuk pembelajaran pemrograman Python')
    while True:
        print('1. Kembali')
        choice = input('Masukkan pilihan Anda: ')
        
        if choice == '1':
            main.main()

        else:
            print('Pilihan tidak valid. Silakan coba lagi.')


if __name__ == '__main__':
    utama()
