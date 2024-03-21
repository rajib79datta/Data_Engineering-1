#!/usr/bin/env python3

import sys
import json
import re
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['twitter']  # Connect to your MongoDB database
collection = db['tweets']  # Connect to your MongoDB collection

# Compile regular expression patterns for the pronouns
pronoun_patterns = [
    re.compile(r'\bhan\b', re.IGNORECASE),
    re.compile(r'\bhon\b', re.IGNORECASE),
    re.compile(r'\bden\b', re.IGNORECASE),
    re.compile(r'\bdet\b', re.IGNORECASE),
    re.compile(r'\bdenna\b', re.IGNORECASE),
    re.compile(r'\bdenne\b', re.IGNORECASE),
    re.compile(r'\bhen\b', re.IGNORECASE)
]

# Read input from STDIN (standard input)
for line in sys.stdin:
    try:
        # Parse the JSON tweet
        tweet = json.loads(line)

        # Check if the tweet is a retweet, if yes, skip it
        if 'retweeted_status' in tweet:
            continue

        # Extract text from the tweet
        text = tweet.get('text', '').lower()

        # Check if any pronoun appears in the tweet and emit key-value pair
        for pattern in pronoun_patterns:
            if pattern.search(text):
                # Insert the tweet into MongoDB
                collection.insert_one(tweet)
                print(f"{pattern.pattern}\t1")

    except Exception as e:
        # Print any errors to STDERR (standard error)
        print("Error:", e, file=sys.stderr)

