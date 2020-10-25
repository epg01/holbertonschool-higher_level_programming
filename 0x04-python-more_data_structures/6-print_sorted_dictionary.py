def print_sorted_dictionary(a_dictionary):
    list_orden = sorted(list(zip(a_dictionary.items())))
    for item in list_orden:
        print("{0:s}: {1:s}".format(str(item[0][0]), str(item[0][1])))
