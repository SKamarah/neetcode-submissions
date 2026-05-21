from typing import Dict, List

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    val_list = []
    for values in age_dict.values():
        val_list.append(values)
    return val_list


# do not modify below this line
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35}))
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}))
