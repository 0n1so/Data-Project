import pandas as pd

df = pd.read_csv("Data.csv", index_col = "Name")


group = df.groupby("Type1")

print(group["Height"].mean())