import random
from libs import welcome_message

emyu_posiion = random.randint(1, 4)

welcome_message("SELAMAT DATANG DI GOA EMYU V1")

nama_fans = input("Masukan nama kamu: ")
while nama_fans == "":
    nama_fans = input("isi dulu nama anda: ")

bentuk_goa = "|_|"
goa_kosong = [bentuk_goa] * 4

goa = goa_kosong.copy()
goa[emyu_posiion - 1] = "|0_0|"

goa_kosong = '  '.join(goa_kosong)
goa = '  '.join(goa)

print(f''' Halo {nama_fans}! Coba perhatiin GOA dibawah ini {goa_kosong}''')

pilihan_fans = input("Menurut kamu di GOA nomor berapakah EMYU berada? [1 / 2 / 3 / 4]: ")
while not pilihan_fans.isdigit() or int(pilihan_fans) not in [1, 2, 3, 4]:
    pilihan_fans = input("Pilih dulu dong!! [1 / 2 / 3 / 4]: ")
pilihan_fans = int(pilihan_fans)

confirm_answer = input(f"Kamu yakin jawabannya {pilihan_fans}? [y/n]: ")

if confirm_answer == "n":
    print("Program dihentikan")
    exit()
elif confirm_answer:
    if pilihan_fans == emyu_posiion:
        print(f"{goa} \n Selamat {nama_fans} Kamu benar! posisi EMYU ada di GOA nomor {emyu_posiion} dan pilihanmu adalah goa nomor {pilihan_fans}.")
    else:
        print(f"{goa} \n KAMU KALAH!!! kayaak emyu yang selalu KALAH awkaokwo, EMYU bukan berada disitu tetapi ada di goa nomor {emyu_posiion}, sedangkan kamu memlih GOA nomor {pilihan_fans}")
else:
    print(f"Silakan ulangi programnya")
    exit()
