import os
import json

# Path to the folder containing JSON files
folder_path = r'D:\Semester-2\Period-1\Data Engineering-I\Project-mini\split-1'

# Initialize an empty list to store JSON data
combined_data = []

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        # Load JSON data from the file
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
            print("Content of {}: {}".format(filename, file_content))
            try:
                json_data = json.loads(file_content)
                combined_data.append(json_data)
            except json.JSONDecodeError as e:
                print("Error decoding JSON in file {}: {}".format(filename, e))

# Path to the combined JSON file
combined_file_path = r'D:\Semester-2\Period-1\Data Engineering-I\Project-mini\split-1\combined.json'

# Write combined JSON data to a single file
with open(combined_file_path, 'w', encoding='utf-8') as combined_file:
    json.dump(combined_data, combined_file, indent=4)

print("Combined JSON file saved at:", combined_file_path)
