import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
data=pd.read_csv(r"C:\Users\anka0\Desktop\Data Science with Python\visulalization\assignement.csv")
data=data.sort_values(by=['Date',"ID","Element"]).reset_index(drop=True)

s=0
for day in data["Date"]:
    if (day[5:7])=="02" and int(day[8:10])>28:
        data["Date"][s]=False
    if int(day[8:10])>30:
        data["Date"][s]=False  
    s=s+1
data=data[data["Date"]!=False].reset_index(drop=True)

max_data=data[data["Element"]=="TMAX"].reset_index(drop=True)
min_data=data[data["Element"]=="TMIN"].reset_index(drop=True)
min_temp=[]
min_date=[]
for day in min_data["Date"].str[5:].unique():
    temp=min(min_data[min_data["Date"].str[5:]==day]["Data_Value"])
    min_temp.append(temp)
    min_date.append(day)

min_data_2015=data[(data["Element"]=="TMIN")& (data["Date"].str[0:4]=="2015")].reset_index(drop=True)  
min_temp_2015=[] 
s=0
for day in min_data_2015["Date"].str[5:].unique():
    temp=min(min_data_2015[min_data_2015["Date"].str[5:]==day]["Data_Value"])
    if temp==min_temp[s]:
        min_temp_2015.append(True)
    else:
        min_temp_2015.append(False)
    s=s+1

max_temp=[]
max_date=[]
for day in min_data["Date"].str[5:].unique():
    temp=max(min_data[min_data["Date"].str[5:]==day]["Data_Value"])
    max_temp.append(temp)
    max_date.append(day)
    
max_data_2015=data[(data["Element"]=="TMIN")& (data["Date"].str[0:4]=="2015")].reset_index(drop=True)  
max_temp_2015=[] 
s=0
for day in max_data_2015["Date"].str[5:].unique():
    temp=max(max_data_2015[max_data_2015["Date"].str[5:]==day]["Data_Value"])
    if temp==max_temp[s]:
        max_temp_2015.append(True)
    else:
        max_temp_2015.append(False)
    s=s+1

min_2015 = {'Date': min_date ,
            'Value':min_temp,
        'Cond': min_temp_2015}
 
df_min_2015 = pd.DataFrame(min_2015)
    
max_2015 = {'Date': max_date ,
         'Value':max_temp,
     'Cond': max_temp_2015}
 
df_max_2015 = pd.DataFrame(max_2015)

scatter_min_2015=df_min_2015[df_min_2015["Cond"]==True]["Value"]
scatter_min_2015_date=df_min_2015[df_min_2015["Cond"]==True]["Date"]

scatter_max_2015=df_max_2015[df_max_2015["Cond"]==True]["Value"]
scatter_max_2015_date=df_max_2015[df_max_2015["Cond"]==True]["Date"]

plt.figure()
# observation_dates = np.arange('2017-01-01', '2017-01-09', dtype='datetime64[D]')
# observation_dates = list(map(pd.to_datetime, observation_dates)) # convert the map to a list to get rid of the error
plt.plot(max_date,max_temp,'blue',min_date,min_temp,'red',markersize=1,linestyle='-')

plt.scatter(scatter_max_2015_date,scatter_max_2015,alpha=1,c='black')
plt.scatter(scatter_min_2015_date,scatter_min_2015,alpha=1,c='magenta')
# fill the area between the linear data and exponential data
plt.gca().fill_between(range(len(max_date)), #lenght
                       max_temp, min_temp, #data interval to fill
                       facecolor='grey', 
                       alpha=0.30) #transparency




plt.legend(['Maximum Temperatures', 'Minimum Temperatures','High temperature records broken in 2015','Low temperature records broken in 2015'])
ax = plt.gca()
ax.set_xlabel('Days of Year')
ax.set_ylabel('Temperatures')
ax.set_title("Highest and Lowest Temperatures between 2005-2014 in Ann Arbor, Michigan ")
ax.set_xticks([])
plt.tick_params(top=False, bottom=False, left=True, right=False)

plt.set_figheight(50)
plt.set_figwidth(50)
plt.show()
