import matplotlib.pyplot as plt

x = ['Q1', 'Q2', 'Q3', 'Q4']
y = [1000, 12000, 11000, 8000]
plt.xlabel('Trin')
plt.ylabel('Paris')
plt.title('Name')
#plt.bar(x,y)
plt.plot(x,y, marker ='o', color = 'yellow', linestyle = '--') #marker add dots/points
plt.show()