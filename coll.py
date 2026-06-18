from collections import Counter

def merge_and_sum_counters(dict1, dict2):
   
    merged = Counter(dict1) + Counter(dict2)
   
    return dict(merged)

dict_a = {'apple': 10, 'banana': 5, 'cherry': 15}
dict_b = {'banana': 12, 'cherry': 5, 'dates': 8}


result = merge_and_sum_counters(dict_a, dict_b)
print("Merged Dictionary:", result)
