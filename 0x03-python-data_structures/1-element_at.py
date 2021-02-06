def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx in range(len(my_list)):
        return my_list[idx]
    else:
        None
