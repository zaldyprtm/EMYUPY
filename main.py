from games import mu
from libs import welcome_message, exit_program
from tools import warung
from tools import suhu
import libs

def menu():
    user_option = int(input(f'silahkan pilih menu program: \n1. Games\n2. Warung\n3. Suhu converter \n4. Keluar '))
    

    if user_option == 1:
        mu.start()
    elif user_option == 2:
        warung.main()
        
    elif user_option == 3:
        suhu.start()
        
    elif user_option == 4:
        exit_program()
    else:
      print("silakan pilih angka yang ada di menu!")
    

def main():
    welcome_message()
    menu()


if __name__ == '__main__':
    main()