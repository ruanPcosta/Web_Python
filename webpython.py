#!/usr/bin/python 
import requests
import sys
import urllib.request

site = requests.get(input("Digite o site que voce quer verificar se é válido:\r\n"))
status = site.status_code
site2 = urllib.request.urlopen(input("Digite o site novamente para obter mais infos caso a resposta seja positiva:\r\n"))
server = site2.info()
conteudo = site2.read()

if(status) == 200: print ("Essa página é VÁLIDA >>>>>> (STATUS 200)\r\n Mais informações abaixo\r\n ", "Servidor WEB e Header da página: \r \n",server, "Conteúdo HTML da página:\r\n", conteudo)

else: print ("Essa página é inexistente")
