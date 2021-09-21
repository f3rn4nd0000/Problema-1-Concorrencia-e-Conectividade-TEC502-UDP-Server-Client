#!/usr/bin/env python
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.
import socket
import sys
import argparse
import json
import random
import time
from faker import Faker
import patient
# from http.client import HTTPConnection
host = '0.0.0.0'
data_payload = 16384

def input_data(x):
  for i in range(0,x):
    patient = patient.Patient()
    print(patient.get_json())
    # while True:
    patient.update_json()
    print(patient.get_json())
  return patient

def echo_client(port):
  """ A simple echo client """
  # Create a UDP socket
  sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  server_address = (host, port)
  print ("Conectando-se a %s porta %s" % server_address)
  message = 'This is the message. It will be repeated.'
  # data = {}
  try:
    # with open("client-data.json",'a') as jsonFile:
      # data = json.load(jsonFile)
    my_patient = patient.Patient()
    # teste = input_data(1).get_json()
    # print('teste=')
    # print(teste)
    # print(type(patient.get_json))
    # print(type(patient.update_json))
    # data_name = patient.get_name()
    # print("data=%s" % data)
  # user_encode_data = json.dumps(data, indent=2).encode('utf-8') # codifica o dictionary data em bytes para ser enviado
    # jsonFile.close()
    # print(type(data))
    print ("Enviando dados em forma de bytes")
    # data_oxigenacao = patient.get_oxigenacao
    while True:
      my_patient.update_json()
      sent = sock.sendto(my_patient.get_json().encode(), server_address)
      print(my_patient.get_json())
      # sent = sock.sendto(patient.toJSON().encode(), server_address)
      # sent2 = sock.sendto(data_update.encode(), server_address)
      # data = patient.update_json()
      # # sent = sock.sendto(data.encode(), server_address)
      time.sleep(1)
  finally:
    print ("Closing connection to the server")
    sock.close()

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Socket Server Example')
  parser.add_argument('--port', action="store", dest="port", type=int, required=True)
  given_args = parser.parse_args()
  port = given_args.port
  echo_client(port)