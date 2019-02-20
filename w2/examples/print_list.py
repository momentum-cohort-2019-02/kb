def print_list(a_list):
    for item in a_list:
        print(item)


def print_list_r(a_list):
    if len(a_list) == 0:
        return
    print(a_list[0], a_list)
    print_list_r(a_list[1:])


print_list_r([
    'Gale',
    'Leslie',
    'Quinn',
    'Chance',
    'Angel',
])
