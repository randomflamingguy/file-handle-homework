file1 = open('hi.txt', 'r')
file2 = open('hi2.txt', 'w')
for line in file1.readlines():
    if not (line.startswith('Coding')):
        print(line)
        file2.write(line)
file2.close
file1.close