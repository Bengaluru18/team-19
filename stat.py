import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
labels = 'health', 'academics', 'renovation',
sizes = [20,50,40]
explode = (0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
userChoice = str(raw_input('\nDo you want to print the graph of score words on output window? (Y/N) :'))
if(userChoice=='Y' or userChoice=='y'):
       plt.show()
