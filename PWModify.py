def generate_variations(word):
    # Initialize the list to store variations
    variations = []

    # List of years to append
    years = [2024, 2023]

    # List of numbers to append
    numbers = [123, 24, 23]

    # Add base word with "!" appended
    variations.append(word + "!")
    
    # Add base word with numbers appended
    for num in numbers:
        variations.append(word + str(num))
        variations.append(word + str(num) + "!")
    
    # Add base word with years appended
    for year in years:
        variations.append(word + str(year))
        variations.append(word + str(year) + "!")
    
    # Add word without any modification (original word)
    variations.append(word)
    
    return variations

def process_words_from_file(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        # Read words from the input file and process each word
        words = file.read().splitlines()
    
    # Open the output file in write mode (this will overwrite any existing content)
    with open(output_filename, 'w') as output_file:
        for word in words:
            # Get variations for each word
            variations = generate_variations(word)
            # Write each variation to the output file, followed by a newline
            for variation in variations:
                output_file.write(variation + '\n')

def main():
    # Input file containing words
    input_filename = 'words'  # Change this to your actual input file name
    # Output file to store generated variations
    output_filename = 'variations.txt'  # Output file to store the variations
    
    # Process words from input file and write the variations to output file
    process_words_from_file(input_filename, output_filename)
    
    print(f"Variations have been written to {output_filename}")

if __name__ == "__main__":
    main()
