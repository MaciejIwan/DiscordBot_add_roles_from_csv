items = [[1, 2, 'name'], [1, 2, 'aaa'], [1, 2, 'sss']]
print(any(flag == 'name' for (_, _, flag) in items))