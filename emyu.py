import random
from libs import welcome_message

while True:
    emyu_position = random.randint(1, 4)

    welcome_message("SELAMAT DATANG DI GOA EMYU V1")

    nama_fans = input("Masukkan nama kamu: ")
    while not nama_fans.strip():
        nama_fans = input("Isi dulu nama anda: ")

    bentuk_goa = "|_|"
    goa_kosong = [bentuk_goa] * 4

    goa = goa_kosong.copy()
    goa[emyu_position - 1] = "|0_0|"

    goa_kosong = '  '.join(goa_kosong)
    goa = '  '.join(goa)

    print(f'''Halo {nama_fans}! Coba perhatikan GOA di bawah ini:\n{goa_kosong}''')

    pilihan_fans = input("Menurut kamu di GOA nomor berapakah EMYU berada? [1 / 2 / 3 / 4]: ")
    while not pilihan_fans.isdigit() or int(pilihan_fans) not in [1, 2, 3, 4]:
        pilihan_fans = input("Pilih dulu dong!! [1 / 2 / 3 / 4]: ")
    pilihan_fans = int(pilihan_fans)

    confirm_answer = input(f"Kamu yakin jawabannya {pilihan_fans}? [y/n]: ")

    if confirm_answer.lower() == "n":
        print("Program dihentikan")
        break
    elif confirm_answer.lower() == "y":
        if pilihan_fans == emyu_position:
            print(f"{goa}\nSelamat {nama_fans}! Kamu benar! Posisi EMYU ada di GOA nomor {emyu_position} dan pilihanmu adalah GOA nomor {pilihan_fans}.")
        else:
            print(f"{goa}\nKamu KALAH!!! Seperti EMYU yang selalu KALAH, EMYU tidak berada di sana, tetapi ada di GOA nomor {emyu_position}, sedangkan kamu memilih GOA nomor {pilihan_fans}.")
    else:
        print("Input tidak valid.")
        break

    main_lagi = input("\n\nMau lanjut main game lagi? [y/n]")
    if main_lagi.lower() == "n":
        break

print("Program Selesai")
