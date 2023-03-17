import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("../../database/googleplaystore.csv")

df = df.assign(Installs = pd.to_numeric(df["Installs"].str.replace("[^0-9]", "",regex=True)))
# df.loc[df["Size"] == "Varies with device", "Size"] = ""
# df.Size = df.Size.str.replace("M","000000",regex=True)
# df.Size = df.Size.str.replace("k","000",regex=True)
# df = df.assign(Size = pd.to_numeric(df["Size"].str.replace("[^0-9]", "",regex=True)))
df = df.assign(Price = pd.to_numeric(df["Price"].str.replace("[^0-9]", "",regex=True)))
df = df.assign(Price = df.Price/100)

df2 = df.drop_duplicates(subset=["App"], keep="first").reset_index(drop=True)

df_top = df2.sort_values(["Price","Installs"], ascending=[False,False])


# print(table) the unique names of all categories

#print(pd.unique(df_top["Category"]))

# plot a bar chart for categories with the total number of installing numbers in each category 

# df_catt = df_top.groupby("Category")["Installs"].sum()
# print(df_catt.shape) 
# df_catt.plot(kind="bar")
# plt.show()

# plot a bar chart for the total prices of each paid app in each category ( the sum of all prices in the same category)
df3 = df2[df2["Price"]>0]

# df_catt = df3.groupby("Category")["Price"].sum()
# print(df_catt) 
# df_catt.plot(kind="bar")
# plt.show()

# plot a bar chart of the total profit of each category by multiplying the price by the number of installs


df3["Prodotto"] = df3["Price"] * df3["Installs"]
df_catt = df3.groupby("Category")["Prodotto"].sum()
print(df_catt)
df_catt.plot(kind="bar")
plt.show()


