from bs4 import BeautifulSoup as soup
import requests

#Initializing required variables
data = []
json_data = []
site = 'http://www.dncc.gov.bd/site/page/c0b6953f-16d3-405b-85e9-dece13bb98de/Location-and-Area'
html = requests.get(site)
soup = soup(html.text, "html.parser")
#we're getting all the data from a table in the DNCC website
for tr in soup.find_all('tr'):
    td = [td for td in tr.stripped_strings]
    data.append(td)

#This will remove the header the table
for i in data:
    if i == ['ক্রমিক নং', 'ওয়ার্ড নং', 'ওয়ার্ডের আওতাধীন এলাকা']:
        data.remove(i)


#delete the index number
for i in data:
    del i[0]

#transform into JSON
for i in data:
    ward_data = {
        'ward': i[0],
        'area': i[1],
        'city_corporation': 'Dhaka North'
    }
    json_data.append(ward_data)
print(json_data)
