# EstagioPF
Repository created to store codes for the Federal Police 01/2021 internship selection process.
## Problema 1
Dado uma lista de dicionários (chave/valor) Python, verifique se existe a chave 'nome', e caso exista, salve o valor dessa chave em uma segunda lista, de modo que não haja repetição de valores na segunda lista.
### Solução
Para a solução deste 
[Problema 1](https://github.com/markinlimac/EstagioPF/blob/main/problema1.py), foi utilizado uma condição de loop para andar de chave em chave do dicionario, a cada chave verifica se ela é do tipo nome, caso seja, é utilizado outra condição de loop para verificar todos os valores da lista que recebera os novos valores, a fim de verificar se o valor que sera inserido ja existe na lista, caso exista, um contador ira iterar para fazer a verificação no final, caso o verificador ao fim do loop seja igual a 0 é porque o valor ainda não existe, adicionando assim o valor ao final da lista.
## Problema 2
Dado um arquivo csv com delimitador ';' e com o seguinte cabeçalho: id;nome;telefone;idade. 
Retorne uma lista com os registro ordenados por nome.
### Solução
Para a solução deste [Problema 2](https://github.com/markinlimac/EstagioPF/blob/main/problema2.py), foi utilizado duas bibliotecas `csv` e `operator`, uma para fazer a manipulação do arquivo csv e outra para fazer a ordenação por nome. Com o arquivo csv aberto, define-se um leitor csv para fazer a manipulação dos dados do arquivo, com a função sorted da biblioteca operator é realizado a ordenação utilizando a segunda coluna do arquivo `(key=operator.itemgetter(1))`. Após isso é retirado o ultimo elemento da lista, pois sempre será o cabeçalho, então imprime-se as linhas ordenadas.