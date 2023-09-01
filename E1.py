import re
# Open text file
with open('file_to_read.txt', 'r', encoding='utf-8') as file:
    # Read file contents
    text = file.read()
# Keywords to look for
keyword = 'terrible'
# Use regular expressions to find keywords
pattern = re.compile(r'\b' + re.escape(keyword) + r'\b')
matches = pattern.findall(text)

# Count the number of keyword occurrences
count = len(matches)

# Replace keywords according to the number of times
new_text = text
for i in range(count):
    if (i + 1) % 2 == 1:
        new_text = pattern.sub('marvellous', new_text, count=1)
    else:
        new_text = pattern.sub('pathetic', new_text, count=1)

count_marvellous = new_text.count('marvellous')
count_pathetic = new_text.count('pathetic')
print(f'"{keyword}": {count}')

# Create a new text file and save the replaced text
with open('result.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(new_text)
    # Output result
print('The replaced text is saved to the result.txt file.')
