#!/usr/bin/env python3

import sys
import json
import re

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
                print(f"{pattern.pattern}\t1")
    
    except Exception as e:
        # Print any errors to STDERR (standard error)
        print("Error:", e, file=sys.stderr)

