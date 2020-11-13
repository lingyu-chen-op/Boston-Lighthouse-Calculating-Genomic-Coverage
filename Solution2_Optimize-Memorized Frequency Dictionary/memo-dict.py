import pandas as pd
import numpy as np
import time


#load data
loci_data = pd.read_csv("../data/loci.csv")
reads_data = pd.read_csv("../data/reads.csv")

#convert to nparray
loci_position_arr = np.asarray(loci_data["position"])
reads_arr = np.asarray(reads_data)

reads_dict_memo_freq = {} 
coverages = []

start_time = time.time()

# Variables to store overall minimum and maximum of the all covered positions
minimum = float("inf") 
maximum = float("-inf")

# Constructing frequency dictionary, with O(N) & O(N) time and space complexity 
for i in range(len(reads_arr)):
    start_position = reads_arr[i][0]
    end_position = reads_arr[i][0] + reads_arr[i][1] # end_position is not inclusive
    
    if start_position in reads_dict_memo_freq:
        prev_freq = reads_dict_memo_freq[start_position]
        reads_dict_memo_freq[start_position] = prev_freq + 1
    else:
        reads_dict_memo_freq[start_position] = 1
        
    if end_position in reads_dict_memo_freq:
        prev_freq = reads_dict_memo_freq[end_position]
        reads_dict_memo_freq[end_position] = prev_freq - 1
    else:
        reads_dict_memo_freq[end_position] = -1
    
    # tracking minimum & minimum positions
    if start_position < minimum:
        minimum = start_position
    if end_position > maximum:
        maximum = end_position

# init frequency of position "minimum - 1" as 0, for easy to iterate below
reads_dict_memo_freq[minimum - 1] = 0

# constructing the frequency dict, with O(maximum - minimum) to O(N) time complexity
for i in range(minimum, maximum):
    if i in reads_dict_memo_freq:
        freq = reads_dict_memo_freq[i]
        reads_dict_memo_freq[i] = freq + reads_dict_memo_freq[i - 1]
    else:
        reads_dict_memo_freq[i] = reads_dict_memo_freq[i - 1]

# append coverages
for i in range(len(loci_position_arr)):
    position = loci_position_arr[i]
    if position in reads_dict_memo_freq:
        coverages.append(reads_dict_memo_freq[position])
    else:
        coverages.append(0)

loci_data["coverage"] = coverages
loci_data.to_csv('./loci.csv')

print("Runtime for Solution2-Optimized is : ")
print(time.time() - start_time)
# Runtime for Solution2-Optimized is : 
# 55.60039210319519