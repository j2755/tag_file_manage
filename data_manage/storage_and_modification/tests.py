import pandas as pd
import csv
def initialize_test_csv():
	csv_columns = ['No','Name','Country']
	dict_data = [
	{'No': 1, 'Name': 'Alex', 'Country': 'India'},
	{'No': 2, 'Name': 'Ben', 'Country': 'USA'},
	{'No': 3, 'Name': 'Shri Ram', 'Country': 'India'},
	{'No': 4, 'Name': 'Smith', 'Country': 'USA'},
	{'No': 5, 'Name': 'Yuva Raj', 'Country': 'India'},
	]
	csv_file = "Names.csv"
	try:
	    with open(csv_file, 'w',newline='') as csvfile:
	        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
	        writer.writeheader()
	        for data in dict_data:
	            writer.writerow(data)
	except IOError:
	    print("I/O error")

def print_test_csv():
	with open('Names.csv',) as csv_file:
	    csv_reader = csv.reader(csv_file, delimiter=',')
	    line_count = 0
	    for row in csv_reader:
	        print(row)



def add_column():
	default_
	with open('Names.csv',) as csv_file:
		csv_reader=csv.reader(csv_file)
		csv_writer=csv.writer(csv_file)
		for row in csv_reader:
			row.append(default_text)
        	# Add the updated row / list to the output file
			csv_writer.writerow(row)


x=pd.read_csv("Names.csv")
print(x)