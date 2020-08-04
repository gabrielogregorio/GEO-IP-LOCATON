import json
from urllib.request import urlopen

try:
    link = "http://ip-api.com/json/45.236.64.4"

    JsonAPI = urlopen(link).read()
    Json = json.loads(JsonAPI)

    print("IP:           | "+Json["query"])
    print("Cidade:       | "+Json["city"])
    print("Estado (UF):  | "+Json["region"])
    print("Pais:         | "+Json["country"])
    print("Latitude:     | "+str(Json["lat"]))
    print("Longitude:    | "+str(Json["lon"]))

except:
    print('Erro!')
