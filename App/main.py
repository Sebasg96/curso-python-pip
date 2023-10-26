import utils
import read_csv  as read
import charts

def run():
  data = read.read_csv('data.csv') #funcion que trata el csv
  
  #map para extraen values del key indicado 
  data = list(filter(lambda country: country["Continent"] == 'South America',data))
  
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries,percentages)

  country = input('Type country => ')

  result = utils.population_by_country(data,country) #Funcion que deja solo las estadisticas de poblacion
  

  if len(result) > 0: #Para validar que se ponga un pais
    country = result[0] #al retornar lista de diccionarios la posicion devuelve el primer item solo como dic
    labels,values = utils.get_population(country) #funcion que retrona dos valores para graficar
    charts.generate_bar_char(country['Country/Territory'],labels,values)
  
  '''labels,values = utils.world_pop_percentage(data)
  charts.generate_pie_chart(labels,values)'''
  
if __name__ == '__main__':
  run()

# __name__ Dualidad para que el modulo se pueda ejecutar desde otro archivo o desde terminal.
