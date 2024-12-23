import time
import platform
import requests
import os

os.system('pip install requests')


def clear():

    if(platform.system() == "Windows"):
        os.system('cls')
    else:
        os.system('clear')


ip = input("** IP **: ")

print("**! Raininmoonlight !**")

print("Loading...")
time.sleep(2)
clear()



url = f"http://ip-api.com/json/{ip}"

try:
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    if data["status"] == "success":
        ipApi = data.get("query")
        country = data.get("country")
        city = data.get("city")
        latit = data.get("lat")
        longt = data.get("lon")
        org = data.get("org")
        timezone = data.get("timezone")

        print("========== K - IP INFO ==========\n")
        print(f"Ip:  {ipApi} \n")
        print(f"Country: {country}\n")
        print(f"City: {city}\n")
        print(f"Latitude: {latit}\n")
        print(f"Longuitude: {longt}\n")
        print(f"Org: {org}\n")
        print(f"Timezone: {timezone}\n")
        print("=================================\n")



    else:
        print(f"Error: {data.get('message')}")
except requests.exceptions.RequestException as e:
    print(f"Request error: {str(e)}")
