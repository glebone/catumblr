
import requests
import json

#  ^..^ CAT(c) 2014 CATumblr - Weather provider module 
# --------------------------------------------------------
# 31 Jan 2014 glebone@yandex.ru 


url = "http://www.myweather2.com/developer/forecast.ashx?uac=pP9Pz3soUU&output=json&query=%2049.425267,%2032.063599&temp_unit=c"

def get_weather():
	r = requests.get(url)
	weather_json = json.loads(r.text)
	return weather_json["weather"]["curren_weather"][0]["temp"] + " " + weather_json["weather"]["curren_weather"][0]["weather_text"]

