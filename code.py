# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path

#Code starts here

# Data Loading 

data = pd.read_csv(path)

data.rename(columns={'Total':'Total_Medals'}, inplace=True)

print(data.head())

# Summer or Winter

data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'],'Summer',np.where(data['Total_Summer']<data['Total_Winter'],'Winter','Both'))

# print(data.head(5))

better_event = data['Better_Event'].value_counts().idxmax()

print(better_event)

# Top 10

top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

# print(top_countries.head()) 

top_countries.drop(top_countries.index[len(top_countries)-1],inplace=True)

print(top_countries.tail(1))


def top_ten(df,column):
    country_list = []
    country_list = list(df.nlargest(10,column)['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries,'Total_Summer')
print("\n top_10_summer: ", top_10_summer)

top_10_winter = top_ten(top_countries,'Total_Winter')
print("\n top_10_Winter: ",top_10_winter)

top_10 = top_ten(top_countries,'Total_Medals')
print("\n top_10: ",top_10)

common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print("\n common: ",common)


# Plotting top 10

summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

ax = summer_df.plot.bar(x='Country_Name', y='Total_Summer', rot=45)
ax1 = winter_df.plot.bar(x='Country_Name', y='Total_Winter', rot=45)
ax2 = top_df.plot.bar(x='Country_Name', y='Total_Medals',rot=45)

# Top Performing Countries

summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df.ix[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
summer_max_ratio, summer_country_gold

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df.ix[winter_df['Golden_Ratio'].idxmax(), 'Country_Name']
winter_max_ratio, winter_country_gold


top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df.ix[top_df['Golden_Ratio'].idxmax(), 'Country_Name']
top_max_ratio, top_country_gold

# Best in the world 

data_1 = data.drop(data.index[len(data)-1])

data_1['Total_Points'] = (data_1['Gold_Total']*3)+(data_1['Silver_Total']*2) + (data_1['Bronze_Total']*1)

# print(data_1.head())


most_points = data_1['Total_Points'].max()
print('most_points: ', most_points)

best_country = data_1.ix[data_1['Total_Points'].idxmax(), 'Country_Name']
print('best_country: ', best_country)

# Plotting the best

best = data[data['Country_Name'] == best_country]

best = best[['Gold_Total','Silver_Total','Bronze_Total']]
print(best)

best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)



