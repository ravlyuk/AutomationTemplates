from lxml.html import fromstring
import requests

url = 'https://www.autoscout24.ch/de/autos/bmw--335?make=9&model=1581&page=2&vehtyp=10'
response = requests.get(url=url).text
tree = fromstring(response)
links = tree.xpath('//div[@class="position-relative"]/*/*/a[@data-qa="details-link"]/@href')
print(response)
