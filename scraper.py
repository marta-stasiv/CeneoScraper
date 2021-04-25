import requests

respons = requests.get('https://www.ceneo.pl/93191792#tab=reviews')
print(respons.text)