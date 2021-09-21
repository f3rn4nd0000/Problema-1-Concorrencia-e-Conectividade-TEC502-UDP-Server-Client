import threading
import socket
import logging
import requests
import sys
import argparse
import json
import os
import requests
host = 'localhost'
data_payload = 16384

class MyThreadedServer():

  def __init__(self):
    logging.info('Inicializando servidor')
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (host, 8000)
    self.sock.bind(server_address)
    print("servidor ligado a %s na porta %s" % server_address)
    self.clients_list = []
    print("esperando por clientes")
  # def talkToClient(self, ip):
  #   logging.info("Sending 'ok' to %s", ip)
  #   self.sock.sendto("ok", ip)

  # def talkToClient(self, ip):
  #   requests.post(url, verify=False, json=device_data)
  #   logging.info("Sending 'ok' to %s", ip)
  #   self.sock.sendto("ok", ip)
  
  def addClientToList(self, data, client_address):
    self.clients_list.append(client_address) # adiciona a porta de cada cliente a lista, vai ser útil para fazer a seleção de requests depois, selecionar quando enviar POST e PUT
    return self.clients_list
  
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
    # self.addClientToList(data, client_address) # adiciona o endereço do cliente na lista de clientes
    return data_dict

  def parseIps(self, data, client_address):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    device_data = data.decode()
    data_dict = json.loads(device_data)
    self.addClientToList()
    return self.getClientList()  
  
  def talkToFlask(self, data ,client_address):
    # get_state_of_connections = self.parseIps(data, client_address)
    # data_dict = self.parseData(data, client_address)
        
    # client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # data, client_address = client_socket. self. recvfrom(data_payload)
    # self.connectToSocket(data, client_address)
    # print("Foram recebidos %s dados de %s", (len(data), client_address))
    data_dict = self.parseData(data, client_address)
    device_data = data.decode()
    # data_dict = json.loads(device_data)
    print('data_dict nome', data_dict['nome'])
    url = 'http://c6c3-200-26-255-185.ngrok.io/pacientes'
    print("me derrubaram aqui oooh ", self.getClientList().count(client_address))
    print("enviando dados para o servidor Flask")
    # self.clients_list = self.getClientList()
    # cache_dict = data_dict
    # dict_to_parse 
    def post_request_to_flask():
      post_r = requests.post(url, verify=False, json = device_data)
      print("POST req. status:", post_r.status_code)

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
      # for client in self.getClientList():
        # if(client == client_address):
          # print('PUT request')
          # put_request_to_flask()
        # if(client != client_address):
          # print('POST')
          # post_request_to_flask()
          # self.addClientToList(data, client_address)
        # print('asdasd')
        # if(self.getClient/List().count == 0):
          # print('dsadkiio')
    # else:
      # print('asodiasoioioioioiooioioi')

  def listen_clients(self):
    while True:
      # cached_data, client_address = self.sock.recvfrom(data_payload)
      data, client_address = self.sock.recvfrom(data_payload)
      print("Foram recebidos %s dados de %s" % (len(data), client_address))
      # self.parseData(data, client_address)
      # msg, client = self.sock.recvfrom(data_payload)
      # logging.info('Received data from client %s: %s', client, msg)
      # cache_t = threading.Thread(target=self.talkToFlask, args=(client_address,cached_data))
      # pd_t = threading.Thread(target=self.parseData, args=(data, client_address))
      t = threading.Thread(target=self.talkToFlask, args=(data, client_address))
      t.start()
      
      # cached_data_dict = json.loads(cached_data.decode())
      # data_dict = json.loads(data.decode())
      
      # if(data_dict['nome'] == cached_data_dict['nome'] and data_dict['oxigenacao'] != cached_data_dict['oxigenacao'])
        # t = threading.Thread(target=self.talkToFlask.)
      # args=(client,)
      # pd_t.start()

if __name__ == '__main__':
  # Make sure all log messages show up
  logging.getLogger().setLevel(logging.DEBUG)
  t = MyThreadedServer()
  t.listen_clients()
