import csv
import json


def convert_csv_to_json(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        json_data = [row for row in reader]
        return json.dumps(json_data, indent=4)


print(convert_csv_to_json('data.csv'))

# Результат:
[
    {
        "column1": "value1",
        "column2": "value2",
        "column3": "value3"
    },
    {
        "column1": "value4",
        "column2": "value5",
        "column3": "value6"
    }
]
