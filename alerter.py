#-*-encoding=utf8-*-
import pygame
import requests
import time
import sys
import pygame

def btcchina_ticker():
	res = requests.get("https://data.btcchina.com/data/ticker")
	if res.status_code == 200:
		ticker = {}
		ticker["buy"] = float(res.json()["ticker"]["buy"])
		ticker["sell"] = float(res.json()["ticker"]["sell"])
	return ticker

def view_detail(txt):
	return txt

def huobi_ticker():
	res = requests.get("http://market.huobi.com/staticmarket/detail.html")
	if res.status_code == 200:
		try:
			returned_dict = eval(res.text)
			ticker = {}
			ticker["buy"] = float(returned_dict["buys"][0]["price"])
			ticker["sell"] = float(returned_dict["sells"][-1]["price"])
			return ticker
		except:
			pass
		
	return None

def comp(dic1, dic2, threshold):
	if dic1 and dic2:
		return (dic1["sell"] - dic2["buy"]) > threshold or (dic2["sell"] - dic1["buy"]) > threshold
	else:
		return False

pygame.init()
pygame.mixer.init()
pygame.display.set_mode([640,480])
# pygame.display.iconify()
pygame.time.delay(1000)#等待1秒让mixer完成初始化
pygame.mixer.music.load("e:/flower.mp3")
pygame.mixer.music.set_volume(0.15)

mainloop = True
while mainloop:
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				sys.exit()
	if comp(btcchina_ticker(), huobi_ticker(), 20):
		pygame.mixer.music.play()
		pygame.time.delay(10000)
		pygame.mixer.music.stop()
		pygame.display.quit()
		mainloop = False
	else:
		pygame.time.delay(3000)

