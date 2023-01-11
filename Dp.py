import numpy as np
import random
def matchmistachscore(a,b,x,i,j):
    if i==len(x) or j==len(x[0]):
        return
    else:
        if(b[i-1]==a[j-1]):
            x[i][j]=x[i-1][j-1]+5
            matchmistachscore(a,b,x,i+1,j)
            matchmistachscore(a,b,x,i,j+1)
        else:
            c=max(x[i][j-1],x[i-1][j],x[i-1][j-1])
            if(c==0):
                x[i][j]=0
                matchmistachscore(a,b,x,i+1,j)
                matchmistachscore(a,b,x,i,j+1)
            else:
                x[i][j]=c-4
                matchmistachscore(a,b,x,i+1,j)
                matchmistachscore(a,b,x,i,j+1)

def fillzero(x,i,j):
    if i==len(x):
        return
    x[0][i]=0
    x[i][0]=0
    fillzero(x,i+1,j)

x=np.empty((17,17))
l=["A","C","T","G"]
a=[random.choice(l) for i in range(16)]
b=[random.choice(l) for i in range(16)]
#a=["A","C","A","C","A","C","T","A"]
#b=["A","G","C","A","C","A","C","A"]
fillzero(x,0,0)
matchmistachscore(a,b,x,1,1)














print(a)
print(b)
print(x)
