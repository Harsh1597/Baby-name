import requests
from bs4 import BeautifulSoup

url_b = 'http://www.indianhindunames.com/indian-hindu-boy-name-g.htm'
url_g = 'http://www.indianhindunames.com/indian-hindu-girl-name-g.htm'

def boy():
	letter = raw_input("Enter letter: ")
	url_b = 'http://www.indianhindunames.com/indian-hindu-boy-name-'+ letter +'.htm'
	request = requests.get(url_b)
	soup = BeautifulSoup(request.text,"html.parser")
	data = soup.find_all('div',{'class':'txtcontent'})
	for names in data:
		print names.text

def girl():
	lets = raw_input("Enter letter: ")
	url_g = 'http://www.indianhindunames.com/indian-hindu-girl-name-'+ lets +'.htm'
	r = requests.get(url_g)
	soup = BeautifulSoup(r.text,"html.parser")
	d = soup.find_all('div',{'class':'txtcontent'})
	for i in d:
		print i.text


while True:
	choise = raw_input("1.girl --- 2.boy")
	if choise == 1:
		girl()
	else:
		boy()