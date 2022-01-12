import csv
from datetime import datetime
from fpdf import FPDF
import os

def get_folder_path():
  root_folder = os.getcwd()
  thedate = datetime.today().strftime('%Y-%m-%d')
  new_dir_route = root_folder + '/' + thedate + '/'
  return new_dir_route

def get_queries(filename):
  file = open(filename)
  data = csv.reader(file)

  headers = []
  headers = next(data)
  queries = []

  for row in data:
    queries.append(row[0])

  return queries

def get_chunk(index):
    file1 = open("sdnlist.txt", "r") #opens
    lines = file1.readlines() #converts to list of lines
    precede = 1
    follow = 0
    while lines[index - precede] != "\n":
        precede += 1

    if (index + follow) < len(lines) - 1:
      while lines[index + follow] != "\n":
          follow += 1
    else:
      follow = 0
    start = index - precede + 1
    finish = index + follow
    report = lines[start:finish]
    file1.close()
    return report

def report_not_found(query, operator):
    FORMAT = '%Y%m%d%H%M%S'
    path = query + '_not_found.pdf'
    new_path = '%s_%s' % (datetime.now().strftime(FORMAT), path)

    output_text = 'No instance of ' + query + ' found\n'
    output_text += 'Operator: ' + operator

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 12)
    for line in output_text.splitlines():
        pdf.cell(0, 4, txt = line, ln = 1, align = 'L')
    pdf.output(get_folder_path() +'/' + new_path)

def report_found(index, query, operator):
    FORMAT = '%Y%m%d%H%M%S'
    path = '_' + query + '_sanctions_record_FOUND.pdf'
    new_path = '%s_%s' % (datetime.now().strftime(FORMAT), path)

    record = get_chunk(index)

    output_text = "Query: " + query + "\n\n"
    output_text += "Line: " + str(index) + "\n\n"
    output_text += "Operator: " + operator + "\n\n\n"
    for element in record:
        output_text += element + "\n"

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 12)
    for line in output_text.splitlines():
        pdf.cell(0, 4, txt = line, ln = 1, align = 'L')
    pdf.output(get_folder_path() +'/' + new_path)
