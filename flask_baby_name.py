from flask import Flask
import urllib2
import requests
from bs4 import BeautifulSoup
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Welcome!'

@app.route('/boy/<b>')
def boy(b):
	url_b = 'http://www.indianhindunames.com/indian-hindu-boy-name-'+ b +'.htm'
	request = requests.get(url_b)
	soup = BeautifulSoup(request.text,"html.parser")
	data = soup.find_all('div',{'class':'txtcontent'})
	for names in data:
		return names.text

@app.route('/girl/<g>')
def girl(g):
	url_g = 'http://www.indianhindunames.com/indian-hindu-girl-name-'+ g +'.htm'
	r = requests.get(url_g)
	soup = BeautifulSoup(r.text,"html.parser")
	d = soup.find_all('div',{'class':'txtcontent'})
	for i in d:
		return i.text





if __name__ == '__main__':
    app.run(debug=True)
