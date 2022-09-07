dict1 = {"a": 100, "b": 200, "c": 300}

# dict2 = {}
# for k, v in dict1.items():
#     dict2[v] = k
#
# dict1 = dict2

dict1 = {v: k for k, v in dict1.items()}  # 字典推导式
print(dict1)  # {100:"a",200:"b",300:"c"}
