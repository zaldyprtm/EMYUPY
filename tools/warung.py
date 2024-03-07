import main

def start():
    while True:
        print('Ini Warung')
        main_lagi = input(f'Kembali ke Beranda? [y/n]')
        
        if main_lagi == "y":
            main.menu()
        

if __name__ == '__main__':
    start()