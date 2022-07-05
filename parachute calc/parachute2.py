import numpy as np
from matplotlib import pyplot as plt


#taking inputs
print("enter all dimensions in cm")
dc=int(input("enter your parachutes diameter:\t"))                      #the diameter
gores=int(input("enter the number of gores:\t"))                        #number of spilits of the parachute
spillh=int(input("enter the spill hole diameter:\t"))                        #spill hole the hole on the top
po= input("p for portrait\nl for landscape\nenter paper orientation:\t") #paper orientation
#seemal=int(input("enter seem allowance:\t"))                                 #seem allowance the tolarance for tailoring

r=dc/2          #finding the radius of parachute
rh=spillh/2     #finding the radius of spillhole

if po =="p":
    po = "portrait"
else:
    po = "landscape"

#parachutes walls
a=(4*r/gores) #sine function period
dxpoints = np.linspace(0,(2*r*np.pi)/gores,10000)                   #parachute walls x cordinates
dypoints = np.abs(np.sin(dxpoints/a)*np.cos(dxpoints/a)*r*np.pi)    #parachute walls y cordinates

#spill hole 
shxpoint=np.array([0,(2*r*np.pi)/gores])                    #spill hole line x cordinates
shypoint=np.array([((np.pi*r)/2)-rh,((np.pi*r)/2)-rh])      #spill hole line y cordinates

#horizontal line
zxpoints=np.array([0,(2*r*np.pi)/gores])                    #zero line x cordinates
zypoints=np.array([0,0])                                    #zero line y cordinates

#seem allowance
#d=(4*r*seemal/gores)
#saxpoints = np.linspace(0,((2*r*np.pi)/gores)+(2.6*np.pi),10000)                   
#saypoints = np.abs(seemal*np.sin(saxpoints/d)*np.cos(saxpoints/d)*r*np.pi)
#
#data filtering
np.around(dypoints,5,dypoints)                              #rounding the numbers to get rid of the scientific notation
dypoints[dypoints>shypoint[0]]=0                            #replacing the numbers bigger than the spill hole to 0

#ploting
plt.plot(dxpoints, dypoints,'o',color="black",ms=.1)         #ploting the walls with marker size 1 and as points
#plt.plot(saxpoints, saypoints,'o',color="black",ms=.1)
#plt.plot(shxpoint,shypoint,color="white",linewidth=.25)    #ploting the spill hole access line
plt.plot(zxpoints,zypoints,color="black",linewidth=1)       #ploting the first horizontal line
plt.axis('equal')
plt.xlim(-1,1+((2*r*np.pi)/gores))
plt.ylim(-1,1+((np.pi*r)/2))
plt.gca().set_aspect('equal', adjustable='box')
#plt.ylabel('length=circumference/4')
#plt.xlabel('circumference/gores')
plt.axis("off")
plt.savefig('parachute.pdf',dpi=1000,orientation=po,bbox_inches='tight')
plt.savefig('parachute.png',dpi=1000,orientation=po,bbox_inches='tight')
#plt.show()  #show the plot


