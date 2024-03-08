import matplotlib.pyplot as plt

def generate_bar_chart(labels, values, aux):

  number = aux[0]
  name = aux[1]
  type1 = aux[2]
  type2 = aux[3]
  
  if type2 == '':
    type = 'Type: ' + type1
  else:
    type = 'Types: ' + type1 + ' & ' + type2
  
  fig, ax = plt.subplots()
  bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:purple', 'tab:brown', 'tab:orange']
  ax.bar(labels, values, color = bar_colors)
  ax.set_ylabel('St. Value')
  title = '#'+number + ' ' + name + ' - ' + type
  ax.set_title(title)
  plt.show()