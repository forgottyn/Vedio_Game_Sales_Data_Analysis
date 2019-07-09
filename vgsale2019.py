# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 22:07:09 2019

@author: forgottyn
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import cm

'''
data cleansing
'''
#read data
vgsale = pd.read_csv('vgsales-12-4-2019.csv') 

#minimize missing data effect
vgsale.loc[vgsale['Total_Shipped'].isnull(),'Total_Shipped'] = vgsale[vgsale['Total_Shipped'].isnull()]['Global_Sales'] 
#eliminate null total shipping data
vgsale['Total_Shipped'].fillna(-100)
vgsale = vgsale[vgsale['Total_Shipped'] > 0]

'''
part 1: general 
'''
#Year & shipping
yea_ship = vgsale.groupby('Year').Total_Shipped.sum()
t = range(1976, 2021)
upper = 400
supper = np.ma.masked_where(yea_ship >= upper, yea_ship)
slower = np.ma.masked_where(yea_ship < upper, yea_ship)
slower
fig, ax = plt.subplots()
ax.plot(t, slower, t, supper)
plt.show()

#Genre & shipping
color = cm.inferno_r(np.linspace(.4,.8, 30))

gen_ship = vgsale.groupby('Genre').Total_Shipped.sum().sort_values(ascending=True)
gen_ship[:4]
gen_ship
gen_ship.plot(kind='barh', color = color)


#Platform & shipping
color = cm.inferno_r(np.linspace(.2,.7, 30))
pla_ship = vgsale.groupby('Platform').Total_Shipped.sum().sort_values(ascending=True)
pla_ship
pla_ship[20:].plot(kind='barh', color = color)

#publisher & shipping
fig = plt.figure()
color = cm.inferno_r(np.linspace(.6,.9, 30))
pub_ship = vgsale.groupby('Publisher').Total_Shipped.sum().sort_values(ascending=False)
pub_ship[:20].plot(kind='barh', color = color)
pub_ship[1:20].plot(kind='barh', color = color[10])
#Nintendo is on fire
pub_ship[0] - pub_ship[1:4].sum()

#Developer & Shipping
dev_ship = vgsale.groupby('Developer').Total_Shipped.sum().sort_values(ascending=False)
dev_ship[:25].plot(kind='barh', color = color)
'''
Part 2: Why Activision is not Nintendo
'''
ga_nin = vgsale[vgsale.Publisher == 'Nintendo']
ga_act = vgsale[vgsale.Publisher == 'Activision']
len(ga_nin)
len(ga_act)

#genre
color = cm.inferno_r(np.linspace(.4,.8, 30))
gen_ship = vgsale.groupby('Genre').Total_Shipped.sum().sort_values(ascending=False)
gen_nin = ga_nin.groupby('Genre').Total_Shipped.sum().sort_values(ascending=False)
gen_act = ga_act.groupby('Genre').Total_Shipped.sum().sort_values(ascending=False)

gen_ship[:5].plot(kind='barh', color = color[1], title = "Summary")
gen_nin[:5].plot(kind='barh', color = color[15], title = "Nintendo")
gen_act[:5].plot(kind='barh', color = color[29], title = "Activision")

gen_ship[:5]
gen_nin[:5]
gen_act[:5]

#platform
pla_ship = vgsale.groupby('Platform').Total_Shipped.sum().sort_values(ascending=False)
pla_nin = ga_nin.groupby('Platform').Total_Shipped.sum().sort_values(ascending=False)
pla_act = ga_act.groupby('Platform').Total_Shipped.sum().sort_values(ascending=False)

pla_ship.plot(kind='barh', color = color[1], title = "Summary")
pla_nin.plot(kind='barh', color = color[15], title = "Nintendo")
pla_act.plot(kind='barh', color = color[29], title = "Activision")


'''
Part 3: Region and games
'''
