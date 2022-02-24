import pandas as pd
from multiprocessing import Pool
import time
from matplotlib import pyplot as plt

df = pd.read_csv("C:/Users/Admin/Downloads/14.txt", sep=",", encoding="cp1251")
df = df.dropna()
df = df.drop(df[df['Активные случаи'] == -1].index)
df['Заболели'].apply(lambda x: int(x.replace("'","").strip()))

def max_multiprocess(num_of_proc, df):
    start_time = time.time()
    with Pool(num_of_proc):
        df_copy = df.copy()
        df_copy['Активные случаи'].max()

    end_time = time.time()
    print(end_time - start_time)
    return end_time - start_time


a = max_multiprocess(1, df)
b = max_multiprocess(2, df)
c = max_multiprocess(3, df)
d = max_multiprocess(4, df)
e = max_multiprocess(5, df)
f = max_multiprocess(6, df)
g = max_multiprocess(7, df)
h = max_multiprocess(8, df)
i = max_multiprocess(9, df)
j = max_multiprocess(10, df)

plt.ylabel('y')
plt.xlabel('x')
plt.title('time by number of processes')
plt.plot([0, a, b, c, d, e, f, g, h, i, j], color='blue')
plt.show()

