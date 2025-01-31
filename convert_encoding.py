with open('data.json', 'r', encoding='utf-16') as infile:
    data = infile.read()

with open('data_utf8.json', 'w', encoding='utf-8') as outfile:
    outfile.write(data)
