import numpy as np
import matplotlib.pyplot as plt

#Datasets
eurusd = [66,66,100,71,71,50,100,40,33,66,100,0,100,50,83,66,50,50]
audusd = [58,100,60,80,60,50,50,66,50,20,0,50,100,66,83,100,100,75]

#Histogram
#bins = splits the X axis into tenths
plt.hist(eurusd, bins=10, edgecolor='black')
plt.title("Distribution of EURUSD Weekly Rate of Reactions From S/D Zones")
plt.xlabel('Rate of Zone Reaction (%)')
plt.ylabel('Frequency')

plt.show()

plt.hist(audusd, bins=10, edgecolor='black')
plt.title("Distribution of AUDUSD Weekly Rate of Reactions From S/D Zones")
plt.xlabel('Rate of Zone Reaction (%)')
plt.ylabel('Frequency')

plt.show()