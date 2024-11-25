import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load DataFrame from csv file

df = pd.read_csv('COVID-19_Statistics.csv')
#print(df.head(5))

# Calculate recovery rate

df['Recovery Rate'] = np.round((df['Recovered']/df['Total Cases'])*100,2)
print(df['Recovery Rate'])
recovery_rate = df['Recovery Rate']
# Total cases by country

total_cases_by_country = df.groupby('Country')['Total Cases'].sum()
#print(total_cases_by_country)
print(recovery_rate)
# Creating a Bar Chart

total_cases_by_country.plot(kind='bar', title='Total Cases by Country')
plt.xlabel('Country')
plt.ylabel('Total Cases')
#plt.show()