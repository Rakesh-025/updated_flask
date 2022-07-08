import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Maintenance_cost':500, 'Marketing_cost':90, 'Profit_Margin':65,'Level_of_Course': 2,'Duration_of_coaching_in_Hours': 12})

print(r.json())