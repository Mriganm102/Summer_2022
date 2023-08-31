import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("gun_data.csv", sep=" ", header=None)
print(df)

df.plot(x=0, y=1, kind='scatter')
plt.show()