from nselib import derivatives as dr
import pandas as pd
import matplotlib.pyplot as plt
import time as t
import shutil as sh
import os

time_frame=5  # in minute
x_cor=[]
y_cor=[]
plt.hlines(y=1,xmax=360,xmin=0,color="k",linestyles="--")
plt.hlines(y=2,xmax=360,xmin=0,color="k",linestyles="--")
def pcr():
    
    #  os.remove("data.csv")
    #  os.remove("data11.csv")
    data = dr.option_price_volume_data(symbol="BANKNIFTY",instrument="OPTIDX",option_type="CE",from_date="30-04-2024",to_date="30-04-2024",period='1D')
    data11 = dr.option_price_volume_data(symbol="BANKNIFTY",instrument="OPTIDX",option_type="PE",from_date="30-04-2024",to_date="30-04-2024",period='1D')
    #data=dr.nse_live_option_chain(symbol='NIFTY',expiry_date="01-05-2024",oi_mode="full")
    data=pd.DataFrame(data)
    data11=pd.DataFrame(data11)
    data.to_csv("data.csv")
    data11.to_csv("data11.csv") 
    data=pd.read_csv("data.csv")
    data11=pd.read_csv("data11.csv")
    da=data['EXPIRY_DT'][0]
    data=data[data["EXPIRY_DT"]==da]
    data11=data11[data11['EXPIRY_DT']==da]
    import numpy as np
    a=49477
    r=a%100
    d=a//100
    if r>60:
        st=d*100+100
    else:
        st=d*100
    arr=np.linspace(-5,5,11)
    tstk=arr*100+st
    tstk=np.array(tstk)
    data1=data[data['STRIKE_PRICE'].isin(tstk)]
    data111=data11[data11['STRIKE_PRICE'].isin(tstk)]
    ce=np.sum(data1["OPEN_INT"])
    pe=np.sum(data111["OPEN_INT"])
    pcr=float(pe)/float(ce)
    return pcr
def update_coordinate():
    x=float(input("enter x coordinate:  "))
    y=float(input("enter y coordinates: "))
    return (x,y)
def update_plot(x,y):
    x_cor.append(x)
    y_cor.append(y)
    plt.plot(x_cor,y_cor,'go--')
    plt.draw()
    plt.pause(0.01)
    plt.savefig("plot.png")

for i in range(0,73):
    x=i*time_frame
    y=pcr()
    update_plot(x,y)
    t.sleep(1)
plt.show()
