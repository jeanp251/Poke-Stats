import csv

def read_csv(path):
  # Read a csv file and return a list of dictionaries
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      poke_dict = {key:value for key, value in iterable}
      data.append(poke_dict)
  return data

if __name__ == '__main__':
  data = read_csv('Pokemon.csv')
  print('***'*5)
  print(data[0])