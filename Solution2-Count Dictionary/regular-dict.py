import pandas as pd
import numpy as np
import time


#load data
loci_data = pd.read_csv("../data/loci.csv")
reads_data = pd.read_csv("../data/reads.csv")

#convert to nparray
loci_position_arr = np.asarray(loci_data["position"])
reads_arr = np.asarray(reads_data)

reads_dict = {}
coverages = []

start_time = time.time()

# Constructing count dictionary, with O(N*L) time complexity, and O(N*L) space complexity in the worst case
# where N is the number of lines of reads data, L is average length of every intervals
for i in range(len(reads_arr)):
    start_position = reads_arr[i][0]
    length = reads_arr[i][1]
    for j in range(start_position, start_position + length):
        if j in reads_dict:
            prev_count = reads_dict[j]
            reads_dict[j] = prev_count + 1
        else:
            reads_dict[j] = 1

# Acessing dictionary to get covred times for positions, with O(M) time complexity
# where M is the number of lines of loci  
for i in range(len(loci_position_arr)):
    position = loci_position_arr[i]
    if position in reads_dict:
        coverages.append(reads_dict[position])
    else:
        coverages.append(0)

loci_data["coverage"] = coverages
loci_data.to_csv('./loci.csv')


print("Runtime for Solution2 is : ")
print(time.time() - start_time)
# Runtime for Solution2 is : 
# 114.5739221572876



