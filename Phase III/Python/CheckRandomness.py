import os
import pandas as pd
import numpy as np

filename = "HGtest.fasta"
path = os.getcwd() + "\\" + filename

cnt = 0
df = pd.DataFrame(columns= ["Line","A","T","G","C"])


with open(path ,"r") as fp:
    for line in fp.readlines():
        cnt += 1
        ls = [cnt, line.count("A"),line.count("G"),line.count("T"),line.count("C")]


        numEl = len(ls)

        newRow = pd.DataFrame(np.array(ls).reshape(1,numEl), columns = list(df.columns))

        df = df.append(newRow, ignore_index=True)

print(df)