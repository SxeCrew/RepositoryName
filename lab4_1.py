import json
def find_sum_of_products(data):
    sum = 0
    for item in data:
        sum += item["score"] * item["weight"]
    return round(sum, 3)


with open("data.json") as f:
    data = json.load(f)

print(find_sum_of_products(data))