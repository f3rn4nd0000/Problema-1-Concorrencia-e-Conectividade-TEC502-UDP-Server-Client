# Problema-1-Concorrencia-e-Conectividade-TEC502-UDP-Server-Client
Repositório contendo código para comunicação entre dispositivos baseados no protocolo UDP

Como usar:
Obtenha o código deste repositório usando git clone ou fazendo download

Após instalação:
```
cd caminho/do/diretorio
python3 t_server.py --url <digite aqui a url fornecida pelo ngrok>
```
Agora digite o comando abaixo para gerar um novo dispositivo que irá gerar dados fictícios:
```
python3 new_device.py --port 8000
```
Obs: Você pode digitar o comando acima quantas vezes quiser, porém atente-se para o fato de que deve gerar novos terminais.
