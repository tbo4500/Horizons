output_file = open('your_output_file.txt')
for line in output_file:
    terms = line.split()
    if len(terms) != 2:
        print terms
