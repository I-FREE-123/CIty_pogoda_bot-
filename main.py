import requests
import datetime
from pprint import pprint
from pogoda import open_weather_token

def get_weather(city, open_weather_token):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        #pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        lenght_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"])\
            - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        print(f"Погода в городе: {city}\nТемпература: {cur_weather}C\n"
              f"Влажность: {humidity}%\nДавление: {pressure}мм.р.ст\nВетер: {wind}\n"
              f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\n"
              f"Продолжительность дня: {lenght_of_the_day}\n"
              f"Хорошего дня!!!"

              )

    except Exception as ex:
        print(ex)
        print("Проверьте название города: ")

def main():
    city = input("Введите город: ")
    get_weather(city, open_weather_token)


if __name__ =='__main__':
    main()
