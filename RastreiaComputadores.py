__author__ = 'Gabriel Gregório da Silva'
__email__ = 'gabriel.gregorio.1@outlook.com'

import os
import json
from urllib.request import urlopen
import re

def rastrear(ip_endereco):
   try:
        link = "http://ip-api.com/json/"+str(ip_endereco)

        JsonAPI = urlopen(link).read()
        Json = json.loads(JsonAPI)

        return dict(Json)
   except Except as e:
        return {"query":"".format(e), "country":"", "region":"", "city":"","lat":"", "lon":""}


regex = r"(\d*)\s{1,}(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|\*\s*$)\s*([\d\,\w]*|)"
site = input("Digite o endereço do site: ")

print("Rastreando site....\n")
os.system('traceroute -q 1 {} > log'.format(site))

# Abre o arquivo com o registro
arquivo = open('log','r')
arquivo_ler = str(arquivo.read())
arquivo.close()
lista = arquivo_ler.split('\n')

print(lista[0])

id = "{0:^5}".format("pt")
ms = "{0:^11}".format("tempo")
ip = "{0:^17}".format("ip")
pais = "{0:^17}".format("pais")
estado = "{0:^4}".format("sg")
cidade = "{0:^20}".format("cidade")
lat = "{0:^9}".format("lat")
long = "{0:^9}".format("long")

print("[{}] {} | {} | {} | {} | {} | {} | {} | ".format(id, ms, ip, pais, estado, cidade, lat, long))

# Obtem a sequência de Ips e número
itens = re.findall(regex, arquivo_ler)
# Anda por todas as sequências
for item in itens:
    numero = item[0]
    ip = item[1]
    id = "{0:^5}".format(numero)

    if ip.strip() != "*":
        rastreio = rastrear(ip)
        if rastreio['status'] !='fail':
            ms = "{0:<11}".format(item[2])
            ip = "{0:<17}".format(rastreio["query"])
            pais = "{0:<17}".format(rastreio["country"])
            estado = "{0:^4}".format(rastreio["region"])
            cidade = "{0:<20}".format(rastreio["city"])
            lat = "{0:^9}".format(rastreio["lat"])
            long = "{0:^9}".format(rastreio["lon"])
        else:
            ms = "{0:<11}".format("fail")
            ip = "{0:<17}".format(ip)
            pais = "{0:<17}".format("***")
            estado = "{0:^4}".format("***")
            cidade = "{0:<20}".format("***")
            lat = "{0:^9}".format("***")
            long = "{0:^9}".format("***")



        print("[{}] {} | {} | {} | {} | {} | {} | {} | ".format(id, ms, ip, pais, estado, cidade, lat, long))
    else:
        print("[{}] - ************* {}".format(id, ip))



# print("https://www.google.com.br/maps/search/"+lat+","+lon+"\n")