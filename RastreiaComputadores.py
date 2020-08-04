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

        return "IP: "+ Json["query"] + ", " + Json["country"] + ", "+ Json["region"]  + "," + Json["city"] + ", lat: " + str(Json["lat"]) + ", long: " + str(Json["lon"])
   except:
        return str(ip_endereco) + " impossivel rastrear esse endereço!"

regex = r"(\d*)\s{1,}(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|\*\s*$)"
site = input("Digite o endereço do site: ")

print("Rastreando site....")
os.system('traceroute -q 1 {} > log'.format(site))

# Abre o arquivo com o registro
arquivo = open('log','r')
arquivo_ler = str(arquivo.read())
arquivo.close()

# Obtem a sequência de Ips e número
itens = re.findall(regex, arquivo_ler)

# Anda por todas as sequências
for item in itens:
    numero = item[0]
    ip = item[1]
    if ip.strip() != "*":
        print("[{}]".format(numero), rastrear(ip))
    else:
        print("[{}]".format(numero), ip)


# print("https://www.google.com.br/maps/search/"+lat+","+lon+"\n")