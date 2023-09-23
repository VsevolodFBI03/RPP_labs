import requests
url = 'http://127.0.0.1:5000/v1/add/region'
data = {
'id': 54,
'name': 'NSK'
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())

url_1 = 'http://127.0.0.1:5000/v1/add/tax-param'
data_1 = {'city_id': 54, 'from_hp_car': 100,
          'to_hp_car': 400, 'from_production_year_car': 2002,
          'to_production_year_car': 2012, 'rate': 35}

response_1 = requests.post(url_1, json=data_1)
print(response_1.status_code)
print(response_1.json())

url_2 = 'http://127.0.0.1:5000/v1/add/auto'
data_2 = {'city_id': 54,
          'name': "Lexus", 'horse_power': 238,
          'production_year': 2003}

response_2 = requests.post(url_2, json=data_2)
print(response_2.status_code)
print(response_2.json())

url_3 = 'http://127.0.0.1:5000/v1/auto'
data_3 = {'id': 1}

response_3 = requests.get(url_3, json=data_3)
print(response_3.status_code)
print(response_3.json())