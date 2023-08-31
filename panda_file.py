import pandas as pd
df = pd.read_csv("pdf_text.txt", sep=" ", header=None, names=["Town", "1", "2", "Jul22", "Jul23", "Percent Change"])
df = df.drop(df[df['Town'] == 'MedianSale'].index)
df = df.drop(df[df['Town'] == 'YTDMedian'].index)
df = df.drop(df[df['Town'] == 'Numberof'].index)
df = df.drop(labels=["1", "2"], axis=1)
df = df.reset_index()
df = df.drop(labels='index', axis=1)
df["Town"] = df["Town"].shift(1, axis=0)
df = df.drop(df[df['Town'] == 'YTD'].index)
df = df.drop([0])
df = df.dropna()
df = df.reset_index()
df = df.drop(labels='index', axis=1)
print(df)
file = open("df_to_csv.csv", 'w')
file.truncate()
df.to_csv('df_to_csv.csv')













