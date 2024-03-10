import main

def reamur():
    while True:
        celcius = float(input(f'Masukan suhu dalam celcius : '))
        reamur = (4/5) * celcius
        print(f'suhu dalam reamur adalah', reamur, 'Reamur') 
        covLagi = input(f'Konversi lagi? [y/n]')
        if covLagi == "n":
            suhu()


# fahrenheit
# rumus (9/5) * C
def fahrenheit():
    while True:
        celcius = float(input(f'Masukan suhu dalam celcius : '))
        fahrenheit = (9/5) * celcius
        print(f'suhu dalam fahrenhiet adalah', fahrenheit, 'Fahrenheit')
        covLagi = input(f'Konversi lagi? [y/n]')
        if covLagi == 'n':
            suhu()
        
# kelvin
# rumus C + 273
def kelvin():
    while True:
        celcius = float(input(f'Masukan suhu dalam celcius : '))
        kelvin = celcius + 273
        print(f'suhu dalam kelvin adalah', kelvin, 'Kelvin')
        covLagi = input(f'Konversi lagi? [y/n]')
        if covLagi == 'n':
            suhu()


def suhu():
    while True:
        print(f'\nPROGRAM KONVERSI SUHU \n')
        pilhan_user = int(input(f'Pilih converter suhu yang anda mau:\n \n1. Celcius ke Reamur \n2. Celcius ke Fahrenheit \n3. Celcius ke Kelvin\n4. Keluar\n \nMasukan pilihan anda: '))
        
        if pilhan_user == 1:
            reamur()
        elif pilhan_user == 2:
            fahrenheit()
        elif pilhan_user == 3:
            kelvin()
        else:
            main.main()
            
        
    
    
            

if __name__ == '__main__':
    suhu()
