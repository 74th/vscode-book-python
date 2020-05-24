#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%%
# iris データセットをの読み込み
df = pd.read_csv("./iris.csv")
df.head()

#%%
# Nameごとのヒストグラムの表示
df.hist(by="Name", column="SepalLength", sharex=True, sharey=True)

#%%
sns.pairplot(df, hue='Name')


# %%
