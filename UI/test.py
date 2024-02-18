import requests

BASE_URL = "http://192.168.4.1/"

route_num = 7
start_location = "1138 Bathurst St"

# print(BASE_URL + str(route_num) + ":" + start_location)

r = requests.get(BASE_URL + str(route_num) + ":" + start_location)

print(r.content)