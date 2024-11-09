#!/bin/bash

# Function to generate the variants for a given username
generate_variations() {
    # Split the username into first name and last name based on the dot separator
    IFS='.' read -r first_name last_name <<< "$1"

    # Get the first letter of the first name
    first_initial="${first_name:0:1}"

    # Create variations
    echo "$1"                    # Original username
    echo "${first_initial}.${last_name}"  # First initial + last name
    echo "${first_initial}${last_name}"   # First initial + full last name
}

# Input file containing the list of usernames
input_file="usernames.txt"  # Replace this with your input file

# Output file where new usernames will be written
output_file="modified_usernames.txt"  # Replace this with desired output file name

# Check if the input file exists
if [[ ! -f "$input_file" ]]; then
    echo "Input file '$input_file' not found!"
    exit 1
fi

# Clear the output file before writing new usernames
> "$output_file"

# Read each username from the input file and generate variations
while IFS= read -r username; do
    generate_variations "$username" >> "$output_file"
done < "$input_file"

echo "New usernames have been written to $output_file"
