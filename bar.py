import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
objects = ('health', 'academics', 'renovation')
y_pos = np.arange(len(objects))
performance = [20,50,40]
     
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('June Month Classifier')
plt.show()
