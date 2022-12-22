import requests
from location import get_location

my_location = get_location()  # location is auto-detected with IP-to-location API
city = my_location.get('city')
url_wttr = f'http://wttr.in/{city}'

feed_wttr = requests.get(url_wttr, params='2')  # Change params value as per https://wttr.in/:help
feed_wttr.raise_for_status()

print(feed_wttr.text)
