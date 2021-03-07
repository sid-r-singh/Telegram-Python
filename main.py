import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from time import time
import os

# Plot figure with subplots of different sizes
fig = plt.figure(1)
# set up subplot grid
gridspec.GridSpec(3,3)
# large subplot
plt.subplot2grid((3,3), (0,0), colspan=2, rowspan=2)
plt.locator_params(axis='x', nbins=5)
plt.locator_params(axis='y', nbins=5)
plt.title(label="Value of Pi using Monte Carlo Simulation",  
          fontsize=15,  
          color="blue",
          pad='11.0') 
#Defining the lines of the square:
init = time()
horiz = np.array(range(100))/100.0
y_1 = np.ones(100)
plt.plot(horiz , y_1, 'b')
vert = np.array(range(100))/100.0
x_1 = np.ones(100)
plt.plot(x_1 , vert, 'b')
#Plotting the random points:
import random
inside = 0
i=1
trials=os.getenv('INPUT_NO_TRIALS')
print("trials=",trials)
#print("GH Wokspace",os.getenv(GITHUB_WORKSPACE))
n=int(trials)

#plt.subplot(2, 1, 1)
while (i<=n):
  x = random.random()
  y = random.random()
  if ((x**2)+(y**2))<=1:
    inside+=1
    plt.plot(x , y , 'go')
  else:
    plt.plot(x , y , 'ro')
  i+=1
pi=(4*inside)/n

diff = time() - init

line_labels = ["Item A", "Item B", "Item C"]




#plot 2:
# small subplot 1
plt.subplot2grid((3,3), (0,2))
plt.locator_params(axis='x', nbins=5)
plt.locator_params(axis='y', nbins=5)

x = np.array([0,0,3,3])
y = np.array([10,40,40,10])
textstr="""Program info
Value of pi is:  %1.5f
No. of points: %1.0f
Exec. time:  %3.1fs"""%(pi,n,diff)
plt.xticks([])
plt.yticks([])
plt.text(0.5,30,textstr, verticalalignment="top")
plt.scatter(x,y,alpha=0.2, edgecolors='none', s=30,)


fig.tight_layout()
fig.set_size_inches(w=11,h=7)
fig_name = 'plot.png'
fig.savefig(fig_name)
plt.show()
