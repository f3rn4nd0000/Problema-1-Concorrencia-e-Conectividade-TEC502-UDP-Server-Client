import threading
import socket
import logging
import requests
import sys
import argparse
import json
import os
import requests # biblioteca que serve para se comunicar com API REST
host = 'localhost'
data_payload = 16384 # tamanho máximo permitido para cada pacote

class MyThreadedServer():

  # Inicia uma instancia dessa classe
  def __init__(self):
    logging.info('Inicializando servidor')
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (host, 8000)
    self.sock.bind(server_address)
    print("servidor ligado a %s na porta %s" % server_address)
    self.clients_list = []
    print("esperando por clientes")
  
  # Adiciona um dispositivo a lista que está enviando pacotes para este servidor UDP
  def addClientToList(self, data, client_address):
    self.clients_list.append(client_address) # adiciona a porta de cada cliente a lista, vai ser útil para fazer a seleção de requests depois, selecionar quando enviar POST e PUT
    return self.clients_list
  
  # retorna a lista de dispositivos que estão enviando pacotes para este servidor UDP
  def getClientList(self):
    return self.clients_list

  def connectToSocket(self):
    data, client_address = self.sock.recvfrom(socket.AF_INET, socket.SOCK_DGRAM)
    print("Foram recebidos %s dados de %s", (len(data), client_address))
    self.parseData(data, client_address)
  
  def parseData(self, data, client_address):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    device_data = data.decode() # decodifica os dados que foram enviados em forma de bytes para uma string
    data_dict = json.loads(device_data) # retorna um objeto dicionário para poder ser manipulado posteriormente
    return data_dict

  def talkToFlask(self, data ,client_address, url):
    data_dict = self.parseData(data, client_address)
    device_data = data.decode()
    # data_dict = json.loads(device_data)
    print('data_dict nome', data_dict['nome'])
    #Esta é a URL que estará hospedado a API REST
    url = url+'/pacientes'
    print("me derrubaram aqui oooh ", self.getClientList().count(client_address))
    print("enviando dados para o servidor Flask")
    
    #método que faz POST request para API REST
    def post_request_to_flask():
      post_r = requests.post(url, verify=False, json = device_data)
      print("POST req. status:", post_r.status_code)
    # método que faz PUT request para API REST
    def put_request_to_flask():
      put_r = requests.put(url, verify=False, json = device_data)
      print("POST req. status:", put_r.status_code)

    # método abaixo garante que os dados sejam atualizados, caso contrário faz um POST request para inserir os dados pela primeira vez! 
    if(self.getClientList().count(client_address) == 0):
      post_request_to_flask()
      self.addClientToList(data, client_address)
    else:
      put_request_to_flask()
    print(self.getClientList())

  def listen_clients(self,url):
    while True:
      # cached_data, client_address = self.sock.recvfrom(data_payload)
      data, client_address = self.sock.recvfrom(data_payload)
      print("Foram recebidos %s dados de %s" % (len(data), client_address))
      t = threading.Thread(target=self.talkToFlask, args=(data, client_address, url))
      t.start()
      
if __name__ == '__main__':
  # Execução do programa, a url é passado por argumento de linha de comando
  # Exemplo de execução: python3 t_server.py --url <url>
  parser = argparse.ArgumentParser(description='Threaded Socket Server Example')
  parser.add_argument('--url', action="store", dest="url", type=str, required=True)
  given_args = parser.parse_args()
  url = given_args.url
  logging.getLogger().setLevel(logging.DEBUG)
  t = MyThreadedServer()
  t.listen_clients(url)
