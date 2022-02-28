import random as rd
import matplotlib.pyplot as plt

rd.seed(1235)

# leser inn data fra filen og lagrer de som en liste
data = []
with open('Antall_drinker.txt') as infile:
     for line in infile:
         line = float(line)
         data.append(line)


# ta 100 ulike sampler og finne middelverdi for disse
avreage_list = []
for i in range(100):
    sample = rd.sample(data,30)
    avreage = sum(sample)/len(sample)
    avreage_list.append(avreage)


simulated_avg = sum(avreage_list)/len(avreage_list)
plt.title('Antall drinker 100 utvalg på 30 pax')
plt.hist(avreage_list,label=f'gjenomsnitt: {simulated_avg:.3f}')
plt.legend()
plt.show()




