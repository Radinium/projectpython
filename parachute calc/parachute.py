import math
from turtle import color
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

print("enter all dimensions in millimeter")

#taking inputs
dc=int(input("enter your parachutes diameter:\t"))#the diameter
gores=int(input("enter the number of gores:\t"))
spillh=input("enter the spill hole diameter:\t")#spill hole the hole on the top
seemal=input("enter seem allowance:\t")#seem allowance the tolarance for tailoring
horizontal,vertical=input("enter paper size:\t").split("*") #paper size 
po= input("p for potrait\nl for landscape\nenter paper orientation:\t")


arclen=[]
arcdistance=[]
arclenformula= dc*math.pi*(1/gores)
arclen.append(arclenformula)
rad=np.arange(1,math.pi/2,0.01)

for i in rad:
    arclen.append(math.cos(i)*arclenformula)
    #finding the cosine of all of the radian values that are stored in rad variable
for i in rad:
    arcdistance.append((math.sin(i)*arclenformula)-132)
    #finding the sine of all of the radian values that are stored in rad variable
#==============================================================================================
print("arclength:",arclen)
print("arcdistnace:",arcdistance)



xpoint = np.array([0, arclen[0]])
ypoint = np.array([0,0])
plt.plot(xpoint, ypoint,color="red")
arclen=np.array(arclen)
b=zip(arclen,arcdistance)

plt.show()

"""for i in arclen:
    plt.rcParams["figure.figsize"] = [200, 200]
    plt.rcParams["figure.autolayout"] = True
    x = [0]
    y = [3]
    plt.xlim(0, 5)
    plt.ylim(0, 5)
    plt.grid()
    plt.plot(x, y, marker="o", markersize=20, markeredgecolor="red", markerfacecolor="green")
    plt.show()"""
