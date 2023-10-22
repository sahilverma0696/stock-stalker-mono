import csv
import json

def get_symbols_from_csv(file_path):
    symbols = []
    with open(file_path, 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            symbols.append(row['SYMBOL'])
    return symbols

csv_file_path = './EQUITY_L.csv'
symbol_list = get_symbols_from_csv(csv_file_path)
#print(symbol_list)


api_url = 'http://localhost:8000/api/symbol/'  # Replace with the actual API URL
data = {'symbols': symbol_list}

# Construct the curl command as a string
curl_command_str = (
    f'curl --location --header "Content-Type: application/json" '
    f'--data \'{json.dumps(data)}\' {api_url}'
)

# Print the curl command
print(curl_command_str)