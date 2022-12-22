import json
import requests


def get_ip():
    addr = requests.get('https://api64.ipify.org?format=json').json()
    return addr["ip"]


def get_location():
    ip_address = get_ip()
    location = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": location.get("city"),
        "region": location.get("region"),
        "country": location.get("country_name")
    }
    return location_data
