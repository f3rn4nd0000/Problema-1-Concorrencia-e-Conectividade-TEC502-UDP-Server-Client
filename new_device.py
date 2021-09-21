import socket
import sys
import argparse
import json
import random
import time
from faker import Faker # esse módulo contem os métodos para geração de dados fakes
import patient # importa o múdulo paciente
host = '0.0.0.0'
data_payload = 16384

# Insere dados aleatórios em nossa instância de paciente
def input_data(x):
  for i in range(0,x):
    patient = patient.Patient()
    print(patient.get_json())
    patient.update_json()
    print(patient.get_json())
  return patient


def echo_client(port):
  """ A simple echo client """
  # Cria um socket UDP
  sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  server_address = (host, port)
  print ("Conectando-se a %s porta %s" % server_address)
  message = 'This is the message. It will be repeated.'
  #Cria uma instância da classe paciente
  try:
    my_patient = patient.Patient()
    print ("Enviando dados em forma de bytes")
    # Enquanto o dispositivo estiver funcionando, envia dados!
    while True:
      my_patient.update_json()
      sent = sock.sendto(my_patient.get_json().encode(), server_address)
      print(my_patient.get_json())
      # Intervalo de tempo de 3 segundos para cada pacote ser enviado
      time.sleep(3)
  finally:
    print ("Closing connection to the server")
    sock.close()

# Roda aplicação, parser é apenas para passar argumentos para inicialização do programa via terminal
# O argumento passado é a porta que o servidor UDP estará escutando
if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Socket Server Example')
  parser.add_argument('--port', action="store", dest="port", type=int, required=True)
  given_args = parser.parse_args()
  port = given_args.port
  echo_client(port)