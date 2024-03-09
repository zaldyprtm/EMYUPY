from games import mu
from libs import welcome_message, exit_program
from tools import warung
import libs

def menu():
    user_option = int(input(f'silahkan pilih menu program: \n1. Games\n2. Warung\n3. Keluar \n '))
    

    if user_option == 1:
        mu.start()
    elif user_option == 2:
        warung.main()
        
    elif user_option == 3:
        exit_program()
    else:
      print("silakan pilih angka yang ada di menu!")
    

def main():
    welcome_message()
    menu()


if __name__ == '__main__':
    main()