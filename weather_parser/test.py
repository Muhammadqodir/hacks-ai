import requests as rq
response = rq.get("https://www.gismeteo.ru/diary/206418/2015/10/")
print(response)