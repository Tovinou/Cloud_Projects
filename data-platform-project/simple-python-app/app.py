import json

def read_data():
    with open('data/sample.json', 'r') as file:
        data = json.load(file)
    return data

def print_data():
    data = read_data()
    for item in data:
        print(f"ID: {item['id']}, Name: {item['name']}, Value: {item['value']}")

if __name__ == "__main__":
    print_data()