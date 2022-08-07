#grayscale
import numpy as np
import cv2
from time import sleep
which="Alpha"
img = cv2.imread('MapsPic\Map'+which+'.png', 1)
#m=["$","#","*","!","=",";",":","~","-",",","."," "]
textfile=open('Maps\Map'+which+'.txt',"w")
for i in range(len(img)):
    line=""
    for i1 in range(len(img[0])):
        c=str(img[i,i1])
        c=c[1:]
        c=c[:len(c)-1]
        cs=[]
        nc=[]
        i3=0
        b=""
        for i2 in range(len(c)):
            try:
                p=int(c[i2])
                cs.append(c[i2])
            except:
                jiuefgUHiuyb56=0
            if c[i2]==" ":
                cs.append(" ")
        for i2 in range(len(cs)):
            if cs[i2]==" ":
                if b!='':
                    nc=[int(b)]+nc
                    b=""
            else:
                b=b+str(cs[i2])
        nc=[int(b)]+nc
        if nc==[0,0,0]:
            line=line+"0"
        elif nc==[255,255,255]:
            line=line+"1"
        elif nc==[128,61,0]:
            line=line+"2"
        else:
            print(nc)
    textfile.write(line+"\n")
    print(line)
textfile.close()
