#game tebak kelinci ada dimana

import random
import main

def gas():
    while True:
        rabbit_position = random.randint(1, 5)
        
        goa_kelinci = "|_|"
        jmlh_goa = [kelinci] * 5
        
        goa = jmlh_goa.copy()
        goa[rabbit_position -1] = "🐇"
        
        jmlh_goa = '    '.join(jmlh_goa)
        goa = '   '.join(goa)
        
        print(f'Perhatikan Goa dibawah ini: \n {jmlh_goa}')
        
        pilihan_user = input(f'menurut kamu di goa mana kelinci berada?? [1 / 2 3 / 4 / 5]:')
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    gas()