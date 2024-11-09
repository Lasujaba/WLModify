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

def process_words_from_file(filename):
    with open(filename, 'r') as file:
        # Read words from file and process each word
        words = file.read().splitlines()
    
    # Process each word and generate variations
    all_variations = []
    for word in words:
        variations = generate_variations(word)
        all_variations.append(variations)
    
    return all_variations

def main():
    # File name where words are stored
    filename = 'words'
    
    # Get variations for each word
    all_variations = process_words_from_file(filename)
    
    # Print the variations for each word
    for variations in all_variations:
        for variation in variations:
            print(variation)

if __name__ == "__main__":
    main()
