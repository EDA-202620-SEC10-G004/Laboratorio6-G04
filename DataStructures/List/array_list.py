def new_list():
    newlist = {
        "elements": [],
        "size": 0,
    }
    return newlist

def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list

def size(my_list):
    return my_list["size"]

def first_element(my_list):
    if my_list["size"] == 0:
        return None
    return my_list["elements"][0]

def is_empty(my_list):
    return my_list["size"] == 0

def get_element(my_list, index):
    return my_list["elements"][index]

def remove_first(my_list):
    if my_list["size"] == 0:
        return None

    element = my_list["elements"].pop(0)
    my_list["size"] -= 1

    return element

def remove_last(my_list):
    if my_list["size"] == 0:
        return None

    element = my_list["elements"].pop()
    my_list["size"] -= 1

    return element

def insert_element(my_list, element, pos):
    if pos < 0 or pos > my_list["size"]:
        return None

    my_list["elements"].insert(pos, element)
    my_list["size"] += 1

    return my_list

def is_present(my_list, element, cmp_function):
    size = my_list["size"]

    if size > 0:
        keyexist = False

        for keypos in range(0, size):
            info = my_list["elements"][keypos]

            if cmp_function(element, info) == 0:
                keyexist = True
                break

        if keyexist:
            return keypos

    return -1

def delete_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:
        return None

    my_list["elements"].pop(pos)
    my_list["size"] -= 1

    return my_list

def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= my_list["size"]:
        return None

    my_list["elements"][pos] = new_info

    return my_list

def exchange(my_list, pos1, pos2):
    if pos1 < 0 or pos1 >= my_list["size"]:
        return None

    if pos2 < 0 or pos2 >= my_list["size"]:
        return None

    my_list["elements"][pos1], my_list["elements"][pos2] = (
        my_list["elements"][pos2],
        my_list["elements"][pos1]
    )

    return my_list

def sub_list(my_list, pos, size):
    """
    Retorna una sublista desde 'pos' hasta 'pos + size'
    """
    sub = new_list()
    if my_list is None or size <= 0:
        return sub
        
    for i in range(pos, pos + size):
        if i < my_list["size"]:
            add_last(sub, get_element(my_list, i))
    return sub

def default_sort_criteria(element_1, element_2):
    is_sorted = False
    if element_1 < element_2:
        is_sorted = True
    return is_sorted


def selection_sort(my_list, sort_criteria):
    size = my_list["size"]

    for i in range(size - 1):
        minimum = i

        for j in range(i + 1, size):
            if sort_criteria(
                my_list["elements"][j],
                my_list["elements"][minimum]
            ):
                minimum = j

        if minimum != i:
            exchange(my_list, i, minimum)

    return my_list


def insertion_sort(my_list, sort_criteria):
    for i in range(1, my_list["size"]):
        j = i

        while (
            j > 0
            and sort_criteria(
                my_list["elements"][j],
                my_list["elements"][j - 1]
            )
        ):
            exchange(my_list, j, j - 1)
            j -= 1

    return my_list


def shell_sort(my_list, sort_criteria):
    size = my_list["size"]
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            j = i

            while (
                j >= gap
                and sort_criteria(
                    my_list["elements"][j],
                    my_list["elements"][j - gap]
                )
            ):
                exchange(my_list, j, j - gap)
                j -= gap

        gap //= 2

    return my_list


def merge_sort(my_list, sort_criteria):

    def merge(elements, left, middle, right):
        left_part = elements[left:middle + 1]
        right_part = elements[middle + 1:right + 1]

        i = 0
        j = 0
        k = left

        while i < len(left_part) and j < len(right_part):
            if sort_criteria(left_part[i], right_part[j]):
                elements[k] = left_part[i]
                i += 1
            else:
                elements[k] = right_part[j]
                j += 1
            k += 1

        while i < len(left_part):
            elements[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            elements[k] = right_part[j]
            j += 1
            k += 1

    def merge_sort_recursive(elements, left, right):
        if left < right:
            middle = (left + right) // 2

            merge_sort_recursive(elements, left, middle)
            merge_sort_recursive(elements, middle + 1, right)

            merge(elements, left, middle, right)

    if my_list["size"] > 1:
        merge_sort_recursive(
            my_list["elements"],
            0,
            my_list["size"] - 1
        )

    return my_list


def quick_sort(my_list, sort_criteria):

    def partition(elements, low, high):
        pivot = elements[high]
        i = low

        for j in range(low, high):
            if sort_criteria(elements[j], pivot):
                elements[i], elements[j] = elements[j], elements[i]
                i += 1

        elements[i], elements[high] = elements[high], elements[i]

        return i

    def quick_sort_recursive(elements, low, high):
        if low < high:
            pivot_position = partition(elements, low, high)

            quick_sort_recursive(
                elements,
                low,
                pivot_position - 1
            )

            quick_sort_recursive(
                elements,
                pivot_position + 1,
                high
            )

    if my_list["size"] > 1:
        quick_sort_recursive(
            my_list["elements"],
            0,
            my_list["size"] - 1
        )

    return my_list

def merge_sort(my_list, sort_criteria=default_sort_criteria):
    if my_list["size"] <= 1:
        return my_list

    mid = my_list["size"] // 2
    left = sub_list(my_list, 0, mid)
    right = sub_list(my_list, mid, my_list["size"] - mid)

    left = merge_sort(left, sort_criteria)
    right = merge_sort(right, sort_criteria)

    return merge(left, right, sort_criteria)

def merge(left, right, sort_criteria):
    result = new_list()
    i = j = 0

    while i < left["size"] and j < right["size"]:
        elem_left = get_element(left, i)
        elem_right = get_element(right, j)
        if sort_criteria(elem_left, elem_right):
            add_last(result, elem_left)
            i += 1
        else:
            add_last(result, elem_right)
            j += 1

    while i < left["size"]:
        add_last(result, get_element(left, i))
        i += 1
    while j < right["size"]:
        add_last(result, get_element(right, j))
        j += 1

    return result