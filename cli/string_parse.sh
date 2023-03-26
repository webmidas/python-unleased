#!/bin/bash

# Input string containing key-value pairs separated by commas
input_string="key1=value1, key2=value with spaces, key3=value3"

# Set the field separator to a comma followed by a space
IFS=", "

# Loop through the input string
for pair in $input_string; do
    # Extract the key and value from the key-value pair
    key=$(echo "$pair" | cut -d'=' -f1)
    value=$(echo "$pair" | cut -d'=' -f2-)
    echo "Key: $key, Value: $value"
done

# Reset the field separator to its default value
unset IFS


#!/bin/bash

# Input string containing key-value pairs separated by commas
input_string="key1=value1,key2=value2,key3=value3"

# Loop through the input string
for pair in $(echo "$input_string" | tr ',' ' '); do
    # Extract the key and value from the key-value pair
    key=$(echo "$pair" | cut -d'=' -f1)
    value=$(echo "$pair" | cut -d'=' -f2)
    echo "Key: $key, Value: $value"
done
