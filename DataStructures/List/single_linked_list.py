from DataStructures.List import list_node as node 

def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }

    return newlist

def add_first(my_list, element):
    new_node = node.new_single_node(element)

    if my_list["size"] == 0:
        my_list["first"] = new_node
        my_list["last"] = new_node
    else:
        new_node["next"] = my_list["first"]
        my_list["first"] = new_node

    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    new_node = node.new_single_node(element)

    if my_list["size"] == 0:
        my_list["first"] = new_node
        my_list["last"] = new_node
    else:
        my_list["last"]["next"] = new_node
        my_list["last"] = new_node

    my_list["size"] += 1
    return my_list

def size(my_list):
    return my_list["size"]

def first_element(my_list):
    if my_list["size"] == 0:
        return None
    return my_list["first"]["info"]

def last_element(my_list):
    if my_list["size"] == 0:
        return None
    return my_list["last"]["info"]

def is_empty(my_list):
    return my_list["size"] == 0

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]

    while searchpos < pos:
        node = node["next"]
        searchpos += 1

    return node["info"]

def remove_first(my_list):
    if my_list["size"] == 0:
        return None

    element = my_list["first"]["info"]

    if my_list["size"] == 1:
        my_list["first"] = None
        my_list["last"] = None
    else:
        my_list["first"] = my_list["first"]["next"]

    my_list["size"] -= 1

    return element

def remove_last(my_list):
    if my_list["size"] == 0:
        return None

    element = my_list["last"]["info"]

    if my_list["size"] == 1:
        my_list["first"] = None
        my_list["last"] = None
    else:
        current = my_list["first"]

        while current["next"] != my_list["last"]:
            current = current["next"]

        current["next"] = None
        my_list["last"] = current

    my_list["size"] -= 1

    return element

def insert_element(my_list, element, pos):
    if pos < 0 or pos > my_list["size"]:
        return None

    if pos == 0:
        return add_first(my_list, element)

    if pos == my_list["size"]:
        return add_last(my_list, element)

    new_node = node.new_single_node(element)

    current = my_list["first"]
    current_pos = 0

    while current_pos < pos - 1:
        current = current["next"]
        current_pos += 1

    new_node["next"] = current["next"]
    current["next"] = new_node
    my_list["size"] += 1

    return my_list

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0

    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1

    if not is_in_array:
        count = -1

    return count

def delete_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:
        return None

    if pos == 0:
        remove_first(my_list)
        return my_list

    if pos == my_list["size"] - 1:
        remove_last(my_list)
        return my_list

    previous = my_list["first"]
    current_pos = 0

    while current_pos < pos - 1:
        previous = previous["next"]
        current_pos += 1

    previous["next"] = previous["next"]["next"]
    my_list["size"] -= 1

    return my_list

def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= my_list["size"]:
        return None

    current = my_list["first"]
    current_pos = 0

    while current_pos < pos:
        current = current["next"]
        current_pos += 1

    current["info"] = new_info

    return my_list

def exchange(my_list, pos1, pos2):
    if pos1 < 0 or pos1 >= my_list["size"]:
        return None

    if pos2 < 0 or pos2 >= my_list["size"]:
        return None

    node1 = my_list["first"]
    node2 = my_list["first"]

    current_pos = 0
    while current_pos < pos1:
        node1 = node1["next"]
        current_pos += 1

    current_pos = 0
    while current_pos < pos2:
        node2 = node2["next"]
        current_pos += 1

    node1["info"], node2["info"] = node2["info"], node1["info"]

    return my_list

def sub_list(my_list, pos, num_elements):
    if pos < 0 or num_elements < 0 or pos + num_elements > my_list["size"]:
        return None

    sublist = new_list()
    current = my_list["first"]

    for _ in range(pos):
        current = current["next"]

    for _ in range(num_elements):
        add_last(sublist, current["info"])
        current = current["next"]

    return sublist
def default_sort_criteria(element_1, element_2):
    is_sorted = False
    if element_1 < element_2:
        is_sorted = True
    return is_sorted


def selection_sort(my_list, sort_criteria=default_sort_criteria):
    if my_list["size"] <= 1:
        return my_list

    current = my_list["first"]

    while current is not None:
        minimum_node = current
        runner = current["next"]

        # Buscar el elemento mínimo en el resto de la lista
        while runner is not None:
            if sort_criteria(runner["info"], minimum_node["info"]):
                minimum_node = runner
            runner = runner["next"]

        # Intercambiar únicamente el contenido ("info")
        if minimum_node != current:
            current["info"], minimum_node["info"] = minimum_node["info"], current["info"]

        current = current["next"]

    return my_list

def default_sort_criteria(element_1, element_2):
    is_sorted = False
    if element_1 < element_2:
        is_sorted = True
    return is_sorted

def selection_sort(my_list, sort_criteria=default_sort_criteria):
    if my_list["size"] <= 1:
        return my_list

    current = my_list["first"]

    while current is not None:
        minimum_node = current
        runner = current["next"]

        while runner is not None:
            if sort_criteria(runner["info"], minimum_node["info"]):
                minimum_node = runner
            runner = runner["next"]

        if minimum_node != current:
            current["info"], minimum_node["info"] = minimum_node["info"], current["info"]

        current = current["next"]

    return my_list


def insertion_sort(my_list, sort_criteria=default_sort_criteria):
    if my_list["size"] <= 1:
        return my_list

    sorted_head = None
    current = my_list["first"]

    while current is not None:
        next_node = current["next"]

        if sorted_head is None or sort_criteria(current["info"], sorted_head["info"]):
            current["next"] = sorted_head
            sorted_head = current
        else:
            search_ptr = sorted_head
            while search_ptr["next"] is not None and not sort_criteria(current["info"], search_ptr["next"]["info"]):
                search_ptr = search_ptr["next"]
            current["next"] = search_ptr["next"]
            search_ptr["next"] = current

        current = next_node

    my_list["first"] = sorted_head
    last_ptr = sorted_head
    while last_ptr is not None and last_ptr["next"] is not None:
        last_ptr = last_ptr["next"]
    my_list["last"] = last_ptr

    return my_list


def shell_sort(my_list, sort_criteria=default_sort_criteria):
    size = my_list["size"]
    if size <= 1:
        return my_list

    # Crear lista de referencias a los nodos para acceso por indexación eficiente en gaps
    nodes = []
    current = my_list["first"]
    while current is not None:
        nodes.append(current)
        current = current["next"]

    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            temp_info = nodes[i]["info"]
            j = i
            while j >= gap and sort_criteria(temp_info, nodes[j - gap]["info"]):
                nodes[j]["info"] = nodes[j - gap]["info"]
                j -= gap
            nodes[j]["info"] = temp_info
        gap //= 2

    return my_list

def merge_sort(my_list, sort_criteria=default_sort_criteria):
    if my_list["size"] <= 1:
        return my_list

    mid = my_list["size"] // 2
    left = new_list()
    right = new_list()

    current = my_list["first"]
    for i in range(my_list["size"]):
        if i < mid:
            add_last(left, current["info"])
        else:
            add_last(right, current["info"])
        current = current["next"]

    left = merge_sort(left, sort_criteria)
    right = merge_sort(right, sort_criteria)

    return merge_ll(left, right, sort_criteria)


def merge_ll(left, right, sort_criteria):
    result = new_list()
    p1 = left["first"]
    p2 = right["first"]

    while p1 is not None and p2 is not None:
        if sort_criteria(p1["info"], p2["info"]):
            add_last(result, p1["info"])
            p1 = p1["next"]
        else:
            add_last(result, p2["info"])
            p2 = p2["next"]

    while p1 is not None:
        add_last(result, p1["info"])
        p1 = p1["next"]

    while p2 is not None:
        add_last(result, p2["info"])
        p2 = p2["next"]

    return result


def quick_sort(my_list, sort_criteria=default_sort_criteria):
    if my_list["size"] <= 1:
        return my_list

    pivot = my_list["first"]["info"]
    less = new_list()
    equal = new_list()
    greater = new_list()

    current = my_list["first"]
    while current is not None:
        val = current["info"]
        if sort_criteria(val, pivot):
            add_last(less, val)
        elif sort_criteria(pivot, val):
            add_last(greater, val)
        else:
            add_last(equal, val)
        current = current["next"]

    sorted_less = quick_sort(less, sort_criteria)
    sorted_greater = quick_sort(greater, sort_criteria)

    result = new_list()
    _concat_list(result, sorted_less)
    _concat_list(result, equal)
    _concat_list(result, sorted_greater)

    return result


def _concat_list(target, source):
    curr = source["first"]
    while curr is not None:
        add_last(target, curr["info"])
        curr = curr["next"]