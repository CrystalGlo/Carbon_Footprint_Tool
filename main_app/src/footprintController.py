import csv
import re
import requests
import time
from main_app.data import carbon
class Utility(object):
    def __init__(self):
        self.statement_year = 0

    def read_file(self, bank_statement):
        file = open(bank_statement[0], 'r')
        file_reader = csv.reader(file, delimiter=',')
        rowList = []
        for row in file_reader:
            for field in row:
                if field.replace("/", "").isdigit() and row not in rowList:
                    year_index = row.index(field)
                    self.statement_year = row[year_index][:4]
                    row[year_index] = self.statement_year + "-" + row[year_index][4:6] + "-" + row[year_index][6:8]
                    rowList.append(row[year_index : year_index + 3])
        return rowList

    def calculate_carbon(self, bank_statement):
        start = time.time()
        carbon_dict = carbon.get_carbon_value()
        categories_dict = carbon.get_categories_lists()
        carbon_statement = []
        for row in bank_statement:
            expenseSource = row[2]
            # remove digits
            expenseSource = re.sub(r"\d", "", expenseSource)
            expenseSource = expenseSource.replace("#","")
            re.sub('[.*?]', '', expenseSource)
            # remove multiple spaces
            expenseSource = re.sub(r"\s+", " ", expenseSource, flags=re.I)
            expenseSource = re.sub(r"\s+$", " ", expenseSource, flags=re.I)
            expenseSource = re.sub(r'\[.*?\]', '', expenseSource)
            print(expenseSource)
            carbonEmission = 0
            # calculate carbon emission
            for key, value in categories_dict.items():
                response = requests.get(str(value))
                if expenseSource.lower() in response.text.lower():
                    carbonFactor = carbon_dict[key]
                    carbonEmission = float(carbonFactor) * abs(float(row[1]))
                    print(key)
                    break
            print(carbonEmission)
            new_line = []
            new_line.append(row[0])
            new_line.append(carbonEmission)
            new_line.append(expenseSource)
            carbon_statement.append(new_line)
        end = time.time()
        print("Temps du calcul= " + str((end-start)/60) + " minutes")
        return carbon_statement

    def get_statement_year(self):
        return self.statement_year

    def calculate_total(self, carbon_statement):
        carbon = 0
        for line in carbon_statement:
            carbon += float(line[1])
        return carbon

# read_file = Utility.read_file
# calculate_carbon = Utility.calculate_carbon
# calculate_total = Utility.calculate_total
