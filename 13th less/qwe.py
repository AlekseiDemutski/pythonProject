import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=eur+usd&oq=eur+usd&aqs=chrome..69i57j0i512l9.3743j1j7&sourceid=chrome&ie=UTF-8'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}

main_page = requests.get(url, headers=headers)

soup = BeautifulSoup(main_page.content, 'html.parser')

convert = soup.findAll('span', {'class': 'DFlfde', 'class': 'SwHCTb', 'data-precision': 2})
convert = float((convert[0].text).replace(',', '.'))
print(convert)










# request = input('Enter your request\n 1 for EUR/USD\n 2 for USD/EUR\n')


