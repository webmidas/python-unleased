import json

# Sample JSON object
json_string = '{"name": "John Doe", "age": 30, "location": {"city": "New York", "state": "NY"}}'

# Parse the JSON string into a Python dictionary
json_data = json.loads(json_string)

# Fetch the value of the 'name' key
name = json_data['name']

# Fetch the value of the 'state' key, which is nested under the 'location' key
state = json_data['location']['state']

print(f"Name: {name}, State: {state}")
