import json

# Sample JSON string
json_string = '{"name": "John Doe", "age": 30, "location": {"city": "New York", "state": "NY"}}'

# Parse the JSON string into a Python dictionary
json_data = json.loads(json_string)

# Function to flatten a dictionary
def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

# Flatten the dictionary and convert it to a string
flat_dict = flatten_dict(json_data)
flat_string = ', '.join([f"{k}: {v}" for k, v in flat_dict.items()])

print(flat_string)
