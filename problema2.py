import csv
import operator

with open('arquivoCSV.csv') as csv_file: # Abrindo arquivo csv
  csv_reader = csv.reader(csv_file, delimiter=';') # Definindo leitor do arquivo csv
  sortedlist = sorted(csv_reader, key=operator.itemgetter(1), reverse=False) # Ordenando lista pelo nome 
  sortedlist.pop() # Retirando cabeçalho da lista
  for line in sortedlist:
    print(line) # Imprimindo linhas ordenadas