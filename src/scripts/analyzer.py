import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns
import pandas as pd

samples_path = os.path.abspath("src/data/samples/")
data_set_1 = pd.read_csv(f"{samples_path}/dataset1.csv", sep=',')
data_set_1.dropna(inplace=True)
data_set_1 = data_set_1.replace(0, np.nan).dropna(axis=0).reset_index(drop=True)

personalities = pd.DataFrame(data_set_1['personality'].value_counts())
plt.figure(figsize=(10,4))
ax = sns.barplot(data=personalities, x=personalities.index, y='personality', width=0.4, order=personalities.sort_values('personality',ascending = False).index)
plt.ylabel('')
for i in ax.containers:
    ax.bar_label(i,)

ages = pd.DataFrame(data_set_1['Age'].value_counts())
plt.figure(figsize=(10,4))
ax = sns.barplot(data=ages, x=ages.index, y='Age')
plt.ylabel('')
for i in ax.containers:
    ax.bar_label(i,)

genres = pd.DataFrame(data_set_1['Gender'].value_counts())
plt.figure(figsize=(8,4))
ax = sns.barplot(data=genres, x=genres.index, y='Gender', width=0.2, order=genres.sort_values('Gender',ascending = False).index)
plt.ylabel('')
for i in ax.containers:
    ax.bar_label(i,)


data_set_2 = pd.read_csv(f"{samples_path}/dataset2.csv", sep='\t')
data_set_2.dropna(inplace=True)
start_rows = len(data_set_2)
data_set = data_set_2.replace(0, np.nan).dropna(axis=0).reset_index(drop=True)
remove_rows = start_rows - len(data_set_2)

countries = pd.DataFrame(data_set_2['country'].value_counts())
countries = countries[countries['country'] >= 4000]
countries = countries[countries.index != 'NONE']
plt.figure(figsize=(18,5))
ax = sns.barplot(data=countries, x=countries.index, y='country', width=0.5, order=countries.sort_values('country',ascending = False).index)
plt.ylabel('')
for i in ax.containers:
    ax.bar_label(i,)

countries = pd.DataFrame(data_set_2['country'].value_counts())
countries = countries[countries['country'] >= 4000]
countries = countries[countries.index != 'NONE']
countries = countries[countries.index != 'US']
countries = countries[countries.index != 'GB']
countries = countries[countries.index != 'CA']
countries = countries[countries.index != 'AU']
plt.figure(figsize=(20,5))
ax = sns.barplot(data=countries, x=countries.index, y='country', width=0.5, order=countries.sort_values('country',ascending = False).index)
plt.ylabel('')
for i in ax.containers:
    ax.bar_label(i,)
