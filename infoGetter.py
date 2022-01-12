import csv

def get_queries(filename):
  file = open(filename)
  data = csv.reader(file)

  headers = []
  headers = next(data)
  queries = []

  for row in data:
    queries.append(row[0])
  print(queries)
  return queries

get_queries('criteria.csv')
