import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

cov19 = pd.read_csv("country_vaccinations.csv")

#Exploragory data Analysis

cov19.describe()
cov19.head()
cov19.tail()
cov19.info()
cov19.count()
cov19.shape
cov19.isnull().sum()
cov19.columns
sns.regplot( y="country",x="iso_code",  data=cov19)
sns.pairplot(cov19)

# statistical Analysis
cov19.mean()
cov19.mode()
cov19.median()

#data preprocessing and handing the missing value

cov19_fillna = cov19
cov19_fillna.fillna(cov19_fillna.mean(), inplace=True)
print(cov19_fillna.isnull().sum())

cov19.info()

#Visualization of datas

sns.regplot( y="daily_vaccinations",x="total_vaccinations",  data=cov19)

sns.regplot( y="daily_vaccinations_raw",x="total_vaccinations",  data=cov19)

sns.scatterplot( y="people_vaccinated",x="total_vaccinations",  data=cov19)

sns.scatterplot(cov19, x='vaccines',y="country")

sns.displot(cov19, x="source_name", kde=True)