from games import mu
from games import rabbit
from libs import welcome_message, exit_program
from tools import warung
from tools import suhu
import kasir
import libs
import about
from tools import weather

def menu():
    user_option = int(input(f'silahkan pilih menu program:\n \n1. Games\n2. Warung\n3. Suhu converter \n4. About \n5. Cuaca \n6. Keluar \n\nMasukan pilihan anda: '))
    
    if user_option == 1:
        mu.ready()
    elif user_option == 2:
        warung.mulai()
        
    elif user_option == 3:
        suhu.suhu()
        
    elif user_option == 4:
        about.about()
        
    elif user_option == 5:
        weather.cuaca()
        
    else: 
        exit()
        
    # else:
    #   print("silakan pilih angka yang ada di menu!")
    

def main():
    welcome_message()
    menu()


if __name__ == '__main__':
    main()