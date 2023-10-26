#Modulo o paquete embebido en python para manejar CSV

import csv

#Funcion para ller CSV con .reader y caracter delimitante
#iteracion para leer cada una de las filas tras procesamiento
def read_csv(path):
  with open(path,'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    headers = next(reader) #lee la primer fila con los encabezados 
    data = [] #lista vacia para llenar con diccionarios
    for row in reader:
      iterable = zip(headers, row) #zip crea union
      country_dict = {key:value for key, value in iterable} #dict comprehension crea un diccionario desde la tupla creada por el zip
      data.append(country_dict) #se llena el diccionario data 
  return data


if __name__ == '__main__':
  data = read_csv('./App/data.csv')
  print(data)
  '''data2 = just_population(data)
  print(data2[1])'''