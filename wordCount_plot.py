import glob
import matplotlib.pyplot as plt

#define filename with file path
file_pattern='/home/rdatta3822/Data_Engineering-1/part-r-00000*'





# Count occurrences of each character
char_count = {}

#loop for matching the pattern
for filename in glob.glob(file_pattern):
 #Read the contents of the file
 with open(filename, 'r') as file:
  data = file.read()

for char in data:
 #if char.isalpha():   # Check if the character is alphabetic
 # char = char.lower(); # Convert the character to lowercase
 if char in char_count:
  char_count[char] +=1;
 else:
  char_count[char] = 1;
#char_count[char] = char_count.get(char, 0) + 1;

# Plotting
plt.bar(char_count.keys(), char_count.values())
plt.xlabel('Character')
plt.ylabel('Frequency')
plt.title('Character(Alaphabetic) Frequency')
plt.show()

