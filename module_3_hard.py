data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(*args):
    total_sum = 0
    for item in args:
        if isinstance(item, int):
            total_sum += item
        elif isinstance(item, str) and len(item) > 0:
            total_sum += len(item)
        elif isinstance(item, (list, tuple, set)):
            total_sum += calculate_structure_sum(*item)
        elif isinstance(item, dict):
            total_sum += calculate_structure_sum(*item.keys())
            total_sum += calculate_structure_sum(*item.values())
    return total_sum


result = calculate_structure_sum(*data_structure)
print(result)