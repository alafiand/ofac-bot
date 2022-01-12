# Matthew's Request: Read each query from input csv/excel file, output found text to PDF with timestamp
from functions import get_folder_path, get_queries, get_chunk, report_found, report_not_found
import os
from datetime import datetime



# STEP 1: Create folder with today's date, download latest sanctions list

import requests
folder_path = get_folder_path()
url = 'https://www.treasury.gov/ofac/downloads/prgrmlst.txt'
r = requests.get(url, allow_redirects=True)
os.makedirs(folder_path)
complete_name = folder_path + 'sdnlist.txt'
open(complete_name, 'wb').write(r.content)


# STEP 2: Parameters

queries = get_queries('criteria.csv')
operator = 'Drew'

# STEP 3: Search


# Loop through each query
for query in queries:
    # setting flag and index to 0
    file1 = open("sdnlist.txt", "r")
    flag = 0
    index = 0

    # Loop line by line of file
    for line in file1:
        index += 1

    # checking string is present in line
        if query.lower() in line.lower():
            flag = 1
            break

 # Step 4: Alerts and Reports
    # checking condition for string found
    if flag == 0: # never found
        # ALERT
        print('String', query, 'Not Found')
        report_not_found(query, operator)

    else:
        # ALERT
        print('SANCTION FOUND!')
        report_found(index, query, operator)


    # closing text file
    file1.close()


