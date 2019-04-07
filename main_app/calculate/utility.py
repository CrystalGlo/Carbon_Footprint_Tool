import csv
import re
from main_app.data import carbon
class Utility(object):

    def read_file(self, statement):
        file = open(statement[0], 'r')
        file_reader = csv.reader(file, delimiter=',')
        arr = []
        for row in file_reader:
            arr.append(row)
        return arr

    def calculate_carbon(self, statement):
        c_data = carbon.get_carbon_value()
        new_data = []
        carbon_result = []
        for k,v in c_data.items():
            new_data.append(v)
        for val in statement:
            x = re.search('[0-9]{2}/[0-9]{2}/[0-9]{4}',val[0])
            if x:
                if val[2]:
                    new_line = []
                    new_line.append(val[0])
                    new_line.append(val[1])
                    new_line.append(val[2])
                    new_line.append(float(new_data[int(val[5])])*float(val[2]))
                    carbon_result.append(new_line)
        return carbon_result

    def calculate_total(self,new_statement):
        carbon = 0
        for line in new_statement:
            carbon += float(line[3])
        return carbon

read_file = Utility.read_file
calculate_carbon = Utility.calculate_carbon
calculate_total = Utility.calculate_total
