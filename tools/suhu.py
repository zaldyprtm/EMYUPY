#program untuk convert celcius ke fahrenheit
import main

def start():
    print(f'Selamat datang di Tools')
    while True:
        print(f'Suhu Converter \n')
        print('1. Convert Suhu \n')
        print('2. Keluar \n')
        choice = int(input(f'masukan pilihan anda \n'))
        
        if choice == 1:
            konversi_suhu()
        elif choice == 2:
            main.main()
        else:
            print(f'Masukan angka yang tersedia')

def konversi_suhu():
    while True:
        celcius = float(input("Celcius= "))
        fahrenheit = celcius * 1.8 + 32
        print(f"Suhu {celcius} C sama dengan {fahrenheit} F\n")
        kembali = input('Koversi lagi? (ya/tidak): ')
        if kembali.lower() != 'ya':
            main()
    
    
if __name__ == '__main__':
    start()