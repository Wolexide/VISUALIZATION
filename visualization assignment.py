# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('covid_19_clean_complete.csv')
print(pd.read_csv)
df = df.drop('Province/State', axis = 1)
df['date'] = pd.to_datetime(df['Date'])

df['month'] = pd.DatetimeIndex(df['date']).month
df['day'] = pd.DatetimeIndex(df['date']).day
df['weekday'] = pd.DatetimeIndex(df['date']).weekday
df['weekofyear'] = pd.DatetimeIndex(df['date']).weekofyear

data = df[['Country/Region', 'Confirmed', 'Deaths', 'Recovered', 'Active', 'WHO Region', 'date', 'month', 'day', 'weekday', 'weekofyear']]

summary = [df['Confirmed'].sum(),df['Deaths'].sum(),df['Recovered'].sum(),df['Active'].sum()]
summary_table = pd.DataFrame(summary,['Confirmed','Deaths','Recovered','Active'],columns=['Sum'])
print(summary_table)

def bar_chart(x_axis, list,title):
    """"This plots a bar chart by accepting some parameters"""
    plt.figure(figsize=(8,5))
    plt.bar(x_axis,list)
    plt.title(title, fontsize= 8)
    plt.show()
    return
#print(bar_chart.__doc__)

x_axis = summary_table.index
my_list = summary_table['Sum']
title = 'A Bar Chart showing the total number of confirmed cases, Deaths, Recovered and Active cases'

bar_chart(x_axis,my_list,title)

month_group = data.groupby('month')[['Confirmed','Deaths','Recovered','Active']].sum()

def line_plot(x_axis,my_list,xticks,label,title):
    """This plots a line graph by accepting some parameters"""
    plt.figure(figsize=(8,5))
    for i in range(len(my_list)):
        plt.plot(x_axis,my_list[i],label=label[i])
    plt.legend()
    plt.xticks(x_axis,xticks)
    plt.title(title,fontsize=6)
    plt.show()

x_axis = month_group.index
my_list = [month_group['Confirmed'],month_group['Deaths'],month_group['Recovered'],month_group['Active']]
xticks = ['Jan','Feb','Mar','Apr','May', 'Jun', 'Jul']
label = ['Confirmed', 'Deaths', 'Recovered', 'Active']
title = 'A line plot of confirmed cases, deaths, recovered and active cases from Jan to July'

#line_plot(x_axis,my_list,xticks,label,title)

region_group = data.groupby('WHO Region')[['Confirmed','Deaths','Recovered','Active']].sum()
region_group

def subplot_pie_chart(x_axis,label,title):
    """This plots a pie chart by accepting parameters"""
    plt.figure(figsize=(15,10))
    for i in range(len(x_axis)):
        plt.subplot(2,2,i+1).set_title(title[i])
        plt.pie(x_axis[i],labels=label)
    plt.show()
    
x_axis = [region_group['Confirmed'],region_group['Deaths'],region_group['Recovered'],region_group['Active']]
label = region_group.index
title = ['Confirmed','Deaths','Recovered','Active Cases']

subplot_pie_chart(x_axis,label,title)