import read_csv
import utils
import charts

def run():
  data = read_csv.read_csv('Pokemon.csv')
  pokemon_name = input('Pokemon name => ')
  poke_dict = utils.get_pokemon(pokemon_name, data)
  stats_dict = utils.get_stats(poke_dict)
  print(poke_dict)
  labels = stats_dict.keys()
  values = stats_dict.values()
  aux = [poke_dict['#'], poke_dict['Name'], poke_dict['Type 1'], poke_dict['Type 2']]
  charts.generate_bar_chart(labels, values, aux)

# Entry point
if __name__ == '__main__':
  run()