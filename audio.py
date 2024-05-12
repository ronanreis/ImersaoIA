import whisper
import datetime
import glob
import os
import json


caminho_geral = os.getcwd() + '/Gravaooes0805/*.gsm'

lista= []

agora = datetime.datetime.now()
# Formata a hora no formato desejado (HH:MM:SS)
hora_formatada = agora.strftime("%H:%M:%S")
print("hora inicio:", hora_formatada)

model = whisper.load_model('medium')

for filename in glob.glob(caminho_geral):
    nome = filename.split('-')
    sub_nome= nome[0].split('/')
    data_evento = sub_nome[7]
    codigo_ligacao = str(nome[len(nome) -2])

    result = model.transcribe(filename)

    texto =  result['text']

    dicionario = {}
#     
#     # Adiciona um novo registro ao dicionário
#     
    dicionario['data_evento'] = data_evento
    dicionario['codigo_ligacao'] = codigo_ligacao
    dicionario['texto'] =  texto

    lista.append(dicionario)    


agora = datetime.datetime.now()
hora_formatada = agora.strftime("%H:%M:%S")

#   # Converte o dicionário para JSON
json_dados = json.dumps(lista, indent=4, ensure_ascii=False)

# Salva o JSON em um arquivo
with open("dados.json", "w", encoding='utf8') as arquivo:
    arquivo.write(json_dados)

print("hora fim:", hora_formatada)










# while True:
#     dicionario = {}
#     texto = input("Digite o texto (ou deixe em branco para sair): ")
#     if not texto:
#         break

#     titulo = input("Digite o título: ")

#     # Adiciona um novo registro ao dicionário
#     dicionario['texto'] =  texto
#     dicionario['titulo'] = titulo

#     lista.append(dicionario)
    

  




# print("Registros inseridos:")
# # for chave, valor in meus_registros.items():
# #   print(f"ID: {chave}, Título: {valor}")



