import matplotlib.pyplot as plt

#list to store the data
snowfall_data = []

#opens the file and reads the lines it needs
with open('snowfall.csv') as infile:
    infile.readline()#removes the header
    for line in infile.readlines():
        temp_line = line.strip().split(',')
        if temp_line[2] == 'NA':
            new_line = 0
        else:
            new_line = float(temp_line[2])
        snowfall_data.append(new_line)
print(snowfall_data)

plt.boxplot(snowfall_data)
plt.title('Snowfall')
plt.ylabel('Snømengde i tommer')
plt.show()