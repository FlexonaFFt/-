first_numbers_list = input().split()
second_numbers_list = input().split()

# def common_elements(lst1, lst2):
#     return len(set(lst1) & set(lst2))

# def common_elements(lst1, lst2):
#     set1 = set(lst1)
#     set2 = set(lst2)
#     common_set = set1.intersection(set2)
#     return len(common_set)

def common_elements(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    common_set = set1.intersection(set2)
    return len(common_set)

print(common_elements(first_numbers_list, second_numbers_list))