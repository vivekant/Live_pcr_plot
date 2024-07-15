from nselib import derivatives as dr
import matplotlib.pyplot as plt
import time as t
import os
import numpy as np
import pandas as pd

name="NIFTY"
strikeprice=24400
timeframe=1 # in minute

x_cor=[]
y_cor=[]
xx=np.linspace(0,360,73)
plt.hlines(y=1,xmax=360,xmin=0,color="k",linestyles="--")
plt.hlines(y=2,xmax=360,xmin=0,color="k",linestyles="--")
def get_pcr():
    data=dr.nse_live_option_chain(name,expiry_date="18-07-2024",oi_mode="full")
    data=pd.DataFrame(data)
    data.to_csv("data.csv")
    data=pd.read_csv("data.csv")
    a=strikeprice
    r=a%50
    s=a//50
    if r<25:
        tstk=s*50
    else:
        tstk=s*50+50
    n_rows=10#except strike
    arr=np.linspace(-int(n_rows/2),int(n_rows/2),11)
    tstk=arr*50+tstk
    
    data=data[data['Strike_Price'].isin(tstk)]
    ce=np.sum(data["CALLS_OI"])
    pe=np.sum(data["PUTS_OI"])
    pcr=pe/ce
    arr=np.array(data["Fetch_Time"])   
    t=arr[0]
    return [pcr,t]
def update_plot(x,y):
    x_cor.append(x)
    y_cor.append(y)
    plt.plot(x_cor,y_cor,'g.--')
    plt.draw()
    plt.savefig("pcrvalue.png")
    plt.pause(timeframe*60)
    

    
for i in range(1,len(xx)):
    x=xx[i]
    d=get_pcr()
    y=d[0]
    print("pcr  value=",y,"   at ",d[1])
    pcrdata=pd.read_csv("pcrd.csv")
    pcrdata.loc[len(pcrdata)]=d
    pcrdata.to_csv("pcrd.csv",index=False)
    update_plot(x,y)  
    
plt.show()