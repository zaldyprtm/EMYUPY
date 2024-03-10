import main

def about():
    print('\nSelamat datang di Program MuzalPra untuk pembelajaran pemrograman Python')
    while True:
        print('1. Kembali')
        choice = input('Masukkan pilihan Anda: ')
        
        if choice == '1':
            main.main()

        else:
            print(f'invalid number')


if __name__ == '__main__':
    about()
