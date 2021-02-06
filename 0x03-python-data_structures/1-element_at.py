def element_at(my_list, idx):
    try:
        if idx < 0:
            return None
        elif my_list[idx]:
            return my_list[idx]
    except IndexError:
            return None
