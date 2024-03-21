#!/usr/bin/env python3

import sys
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['twitter']  # Connect to your MongoDB database
collection = db['tweets']  # Connect to your MongoDB collection

# Initialize variables to keep track of the current pronoun and count
current_pronoun = None
current_count = 0

# Process input from STDIN (standard input)
for line in sys.stdin:
    # Split the input into key and value
    pronoun, count_str = line.strip().split('\t', 1)
    
    # Convert count from string to integer
    count = int(count_str)
    
    # If it's the first iteration or we're still on the same pronoun
    if current_pronoun == pronoun:
        current_count += count
    else:
        # If it's a new pronoun, output the previous pronoun's count
        if current_pronoun:
            print(f"{current_pronoun}\t{current_count}")
        
        # Update variables for the new pronoun
        current_pronoun = pronoun
        current_count = count

# Output the last pronoun's count
if current_pronoun:
    print(f"{current_pronoun}\t{current_count}")

