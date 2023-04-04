from functools import reduce

my_list = [1, 2, 3, 4, 5]
result_map = list(map(lambda x: x * 2, my_list))
print(result_map)  

result_filter = list(filter(lambda x: x % 2 == 0, my_list))
print(result_filter) 

result_reduce = reduce(lambda x, y: x * y, my_list)
print(result_reduce)


