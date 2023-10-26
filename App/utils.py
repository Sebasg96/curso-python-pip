def get_population(country_dict):
  #se crea un diccionario nuevo asociando cada key al value buscado
  population_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
  }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels,values #retorna dos valores para graficar
    

def population_by_country(data,country):
  result = list(filter(lambda item:item['Country/Territory'] == country, data))
  return result
#filter que crea lista que contiene diccionario con el criterio del pais buscado 

#Maps para crear diccionarios con funcion anonima lambda que trae como resultado el value de la key buscada

def world_pop_percentage(data):
  countries = list(map(lambda x: x['Country/Territory'],data))
  result = list(map(lambda x : x["World Population Percentage"],data))
  
  return  countries,result


