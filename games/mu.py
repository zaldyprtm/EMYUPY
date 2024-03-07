import random
from libs import exit_program
import main

def start():
    while True:
        emyu_position = random.randint(1, 4)

    

        bentuk_goa = "|_|"
        goa_kosong = [bentuk_goa] * 4

        goa = goa_kosong.copy()
        goa[emyu_position - 1] = "|0_0|"

        goa_kosong = '  '.join(goa_kosong)
        goa = '  '.join(goa)

        print(f'''Coba perhatikan GOA di bawah ini:\n{goa_kosong}''')

        pilihan_fans = input("Menurut kamu di GOA nomor berapakah EMYU berada? [1 / 2 / 3 / 4]: ")
        while not pilihan_fans.isdigit() or int(pilihan_fans) not in [1, 2, 3, 4]:
            pilihan_fans = input("Pilih dulu dong!! [1 / 2 / 3 / 4]: ")
            pilihan_fans = int(pilihan_fans)

        if pilihan_fans == emyu_position:
            print(f"{goa}\nSelamat {nama_fans}! Kamu benar! Posisi EMYU ada di GOA nomor {emyu_position} dan pilihanmu adalah GOA nomor {pilihan_fans}.")
        else:
            print(f"{goa}\nKamu KALAH!!! Seperti EMYU yang selalu KALAH AWOKWAOKWAO, EMYU ga ada di sana, tetapi ada di GOA nomor {emyu_position}, sedangkan kamu memilih GOA nomor {pilihan_fans}.")

        main_lagi = input("\n\nMau lanjut main game lagi? [y/n]")
        if main_lagi.lower() == "n":
            main.menu()

if __name__ == '__main__':
    start()
    