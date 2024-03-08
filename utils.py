import sys

def get_pokemon(pokemon_name, data):
  pokemon = next((sub for sub in data if sub['Name'] == pokemon_name), None)
  if pokemon is None:
    print('Pokemon not found!!!')
    print('Program finished')
    sys.exit()
  else:
    return pokemon

def get_stats(poke_dict):
  stats = {
    'HP': int(poke_dict['HP']),
    'Attack': int(poke_dict['Attack']),
    'Defense': int(poke_dict['Defense']),
    'Sp. Atk': int(poke_dict['Sp. Atk']),
    'Sp. Def': int(poke_dict['Sp. Def']),
    'Speed': int(poke_dict['Speed'])
  }
  return stats