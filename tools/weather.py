# e8991cd1702a0e52204fccb7c0db77ad
import requests

def get_weather(city, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

def cuaca():
    city = input("Masukkan nama kota: ")
    api_key = 'e8991cd1702a0e52204fccb7c0db77ad'  # Ganti dengan kunci API Anda
    weather_data = get_weather(city, api_key)
    
    if weather_data['cod'] == 200:
        weather = weather_data['weather'][0]['description']
        temp = weather_data['main']['temp']
        print(f"Cuaca di {city}: {weather}")
        print(f"Suhu: {temp}°C")
    else:
        print("Kota tidak ditemukan.")

if __name__ == "__main__":
    cuaca()

