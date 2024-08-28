# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:25:40 2021

@author: lhoes
"""

import random as rnd
import itertools as it
import matplotlib.pyplot as plt
import numpy as np

def norme(a,b):
    return (((b[0]-a[0])**2+(b[1]-a[1])**2)**(1/2))

nb = 7#nombre de points (7 ça commence a lag)
P=[[0,0] for x in range(nb)]
for i in range (nb):
    #[[x,y],[x,y]]
    L= [rnd.randint(-25,25),rnd.randint(-25,25)]
    while norme([0,0],L)>=25:
        L= [rnd.randint(-25,25),rnd.randint(-25,25)]
    P[i] = L


def road(p) :
    nb=len(p)
    route = [0 for x in range (nb)]
    for i in range(nb) : 
        long = norme([0,0],p[i][0])
        for j in range(len(p[i])-1) :
            long+=norme(p[i][j],p[i][j+1])
        long+=norme(p[i][-1],[0,0])
        route[i]=long
        long=0
        
    return route
    
    
def path(P,trajet=1) :
    nb=len(P)
    d = 50
    possible = [i for i in it.permutations(P,round(nb/trajet))]
    print(len(possible))
    if possible[:round(len(possible)/2)].sort() != possible[round(len(possible)/2):].sort() :
        return 
    possible = possible[:round(len(possible)/2)]

    route = road(possible)
    if min(route)>d:
        print('meh')
    
    #print( route,min(route))
    #print(possible[route.index(min(route))],possible)
    affichage(possible,route.index(min(route)),P)
    
    
def affichage(P,n,p):
    plt.figure('Window')
    
    for i in P :
        x=[0] + [i[a][0] for a in range (len(i))] + [0]
        y=[0] + [i[a][1] for a in range (len(i))] + [0]
        plt.plot(x,y,':r',linewidth=0.1)
        
    x=[0] + [P[n][a][0] for a in range (len(i))] + [0]
    y=[0] + [P[n][a][1] for a in range (len(i))] + [0]
    plt.plot(x,y,'-g',linewidth=3)
    
    for i in p :
        plt.plot(i[0],i[1],'k.',markersize=15)
        
    t=np.linspace(0,2*np.pi,1000)
    y=25*np.sin(t)
    x=25*np.cos(t)
    plt.plot(x,y,'b')
        
    plt.plot(0,0,'bo',markersize=15)    
    plt.xlim(-30,30)
    plt.ylim(-30,30)
    plt.grid() 
    plt.show()
    


path(P)