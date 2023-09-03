# selection sort
# time complexity O(n^2)
# space complexity O(1)
# stable

data=[2,4,65,623,3,5,3,2,6,26,87,3,35,6]
def selection_sort(data):
    for i in range(len(data)):
        min_index=i
        for j in range(i+1,len(data)):
            if data[min_index]>data[j]:
                min_index=j
        data[i],data[min_index]=data[min_index],data[i]
    return data
sorted_data=selection_sort(data)
print(sorted_data)