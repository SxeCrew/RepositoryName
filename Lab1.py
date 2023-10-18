
num_list = [1, None, 2, 3, 5, 6]
index_missing = num_list.index(None)
print(num_list)
num_list[index_missing] = 0
a = sum(num_list)
b = len(num_list)
num_list[index_missing] = round(a/b,2)
print(num_list)




