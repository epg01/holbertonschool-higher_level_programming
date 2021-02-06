def element_at(my_list, idx):
    if (idx >= 0) and (idx in set(range(len(my_list)))):
        return my_list[idx]
    else:
        return None
