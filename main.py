import requests
while True:
    input_city=input("Enter the city name:")
    params={"name":input_city,"count":10}
    try:
        response=requests.get("https://geocoding-api.open-meteo.com/v1/search",params=params,timeout=5)
    except requests.exceptions.ConnectionError:
        print("Connection Error")
        exit()
    except requests.exceptions.Timeout:
        print("Timeout Error")
        exit()
    weather_data=response.json()
    if not weather_data.get("results"):
        print("No results found. You have entered wrong spelling")
        break
    else:
        city=weather_data["results"][0]["name"]
        country=weather_data["results"][0]["country"]
        latitude=weather_data["results"][0]["latitude"]
        longitude=weather_data["results"][0]["longitude"]
        print(f"details for the {city},{country} is:")
        print(f"{latitude},{longitude}")
        params={"latitude":latitude,"longitude":longitude,"current_weather":True,"count":10}

        response_1=requests.get("https://api.open-meteo.com/v1/forecast",params=params)
        weather_report=response_1.json()
        current=weather_report["current_weather"]
        print(f"current weather in the {city},{country} is:")
        print(f"current Temperature: {current["temperature"]}C")
        print(f"Current wind speed :{current['windspeed']} mph")
        print(f"Current wind direction :{current['winddirection']}")
        print(f" Daytime : {"yes" if current["is_day"]==True else "no"}")
end=input("Press any key to exit")



