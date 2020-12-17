definedList = {'nome': 'marco', 'cargo': 'estagiario'} # Definindo dicionario
newList = [] # Definindo lista que recebera valores
contador = 0 # Definindo contador

for key in definedList: # Andar de chave em chave do dicionario
  if key == 'nome': # Se a chave for nome
    for value in newList: # Rodar por todos valores da lista que recebera os valores
      if value == definedList[key]: # Se o valor do dicionario ja existir 
        contador += 1 # Adiciona 1 ao contador
    if contador == 0: # Se o contador for igual a 0 é porque o valor não existe na lista
      newList.append(definedList[key]) # Adiciona o valor ao final da lista 

print(newList) # Imprime lista