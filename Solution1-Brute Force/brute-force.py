import pandas as pd
import numpy as np
import time


#load data
loci_data = pd.read_csv("../data/loci.csv")
reads_data = pd.read_csv("../data/reads.csv")

#convert to nparray
loci_position_arr = np.asarray(loci_data["position"])
reads_arr = np.asarray(reads_data)


coverages = []

start_time = time.time()

# Brute Force, with O(M*N) complexity where M & N are the numbers of lines of loci and reads
for i in range(len(loci_position_arr)):
    count = 0
    for j in range(len(reads_arr)):
        if reads_arr[j][0] <= loci_position_arr[i] < reads_arr[j][0] + reads_arr[j][1]:
            count += 1
    coverages.append(count)

loci_data["coverage"] = coverages
loci_data.to_csv('./loci.csv')

print("Runtime for Solution1 is : ")
print(time.time() - start_time)