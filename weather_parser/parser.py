from geopy.geocoders import Nominatim
import json
import requests as rq
from bs4 import BeautifulSoup
headers_={
        'accept': 'application/xml, text/xml, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'referer': 'https://www.gismeteo.ru/diary/206418/2015/10/',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'}

wind_d = ["--", "С", "З", "Ю", "В", "СЗ", "СВ", "ЮЗ", "ЮВ"]
cloud_t = ["--", "sun-bw", "sunc-bw", "suncl-bw", "dull-bw"]
phen_t = ["--", "rain-bw", "snow-bw", "storm-bw"]
f = open('parsed_districts.json', "r")
county_codes = json.load(f)

def getWeather(lat, lon, year, month, day):
	geolocator = Nominatim(user_agent="geoapiExercises")
	location = geolocator.reverse(str(lon)+","+str(lat))
	county = location.raw["address"]["county"].replace(" район", "").replace("ое", "").replace("ий", "")
	print("    "+county)
	county_code = -1
	try:
	    county_code = county_codes[location.raw["address"]["state"]][county]
	    print(county_code)
	except:
	    print("county_code not found!")
	    return False
	response = rq.get(
		"https://www.gismeteo.ru/diary/"+str(county_code)+"/"+str(year)+"/"+str(month)+"/",
		headers=headers_)
	soup = BeautifulSoup(response.text, 'html.parser')
	rows = soup.find("tbody").find_all("tr")
	result = {}
	for row in rows:
		if row.find("td").text == str(day):
			colls = row.find_all("td")
			result["temp"] = colls[1].text
			result["press"] = colls[2].text
			result["cloud"] = 0
			for i in cloud_t:
				if colls[3].prettify().find(i) != -1:
					result["cloud"] = cloud_t.index(i)
			result["phen"] = 0
			for i in phen_t:
				if colls[4].prettify().find(i) != -1:
					result["phen"] = phen_t.index(i)
			result["wind"] = ''.join(x for x in colls[5].text if x.isdigit())
			break
	return result