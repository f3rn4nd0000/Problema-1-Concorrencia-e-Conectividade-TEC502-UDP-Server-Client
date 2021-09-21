# It may run on any other version with/without modifications.
import json
import random
from faker import Faker

# A classe abaixo faz parte da simulação
class Patient:
  #Construtor
  def __init__(self):
    fake = Faker()
    self.first_name = fake.first_name()
    self.last_name = fake.last_name()
    self.oxigenacao = round(random.uniform(90,100),2)
    self.name = ""
    self.gravidade = False
    self.name = ''.join((self.first_name," ",self.last_name))

  # Copia os metadados da nossa instância em uma string formatada como JSON
  def toJSON(self):
      return json.dumps(self, default=lambda o: o.__dict__, 
          sort_keys=True)

  #cria um JSON para ser enviado pelo new_device.py que fará papel de dispositivo UDP.
  def get_json(self):
    # Observe abaixo a lógica para determinar se os dados do paciente serão enviados como grave ou não.
    if(self.gravidade):
      json_content = {
        'nome': self.name,
        'oxigenacao': self.oxigenacao,
        'gravidade': 'grave'
      }
    else:
      json_content = {
        'nome': self.name,
        'oxigenacao': self.oxigenacao,
        'gravidade': 'estavel'
      }
    return json.dumps(json_content)

  # Retorna o nome do paciente
  def get_name(self):
    json_content = {
      'nome': self.name,
    }
    return json.dumps(json_content)  

  #atualiza o JSON com valores de oxigenação diferentes
  def update_json(self):
    self.oxigenacao = round(random.uniform(90,100),2)
    # Abaixo a lógica para determinar se o paciente será apresentado como grave ou não
    if(self.oxigenacao <= 92):
      self.gravidade = True
    if(self.oxigenacao > 92):
      self.gravidade = False

  # Retorna o valor da oxigenação do paciente
  def get_oxigenacao(self):
    return json.dumps(self.oxigenacao)
