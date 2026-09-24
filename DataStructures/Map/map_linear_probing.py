import random

from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf


def new_map(num_elements, load_factor, prime=109345121):
    capacity = mf.next_prime(int(num_elements / load_factor))

    my_map = {
        "prime": prime,
        "capacity": capacity,
        "scale": random.randint(1, prime - 1),
        "shift": random.randint(0, prime - 1),
        "table": [None] * capacity,
        "current_factor": 0,
        "limit_factor": load_factor,
        "size": 0
    }

    return my_map


def default_compare(key, entry):
    if entry is None:
        return False

    if entry["key"] is None:
        return False

    return key == me.get_key(entry)


def is_available(table, pos):
    entry = table[pos]

    if entry is None:
        return True

    if entry["key"] is None:
        return True

    return False


def find_slot(my_map, key, hash_value):
    table = my_map["table"]
    capacity = my_map["capacity"]

    pos = hash_value
    first_available = None

    for _ in range(capacity):

        entry = table[pos]

        if entry is None:
            if first_available is not None:
                return False, first_available

            return False, pos

        if entry["key"] is None:
            if first_available is None:
                first_available = pos

        elif default_compare(key, entry):
            return True, pos

        pos = (pos + 1) % capacity

    return False, first_available


def put(my_map, key, value):
    hash_value = mf.hash_value(my_map, key)

    occupied, pos = find_slot(my_map, key, hash_value)

    if occupied:
        me.set_value(my_map["table"][pos], value)

    else:
        my_map["table"][pos] = me.new_map_entry(key, value)
        my_map["size"] += 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]

        if my_map["current_factor"] > my_map["limit_factor"]:
            rehash(my_map)

    return my_map


def contains(my_map, key):
    hash_value = mf.hash_value(my_map, key)

    occupied, pos = find_slot(my_map, key, hash_value)

    return occupied


def get(my_map, key):
    hash_value = mf.hash_value(my_map, key)

    occupied, pos = find_slot(my_map, key, hash_value)

    if occupied:
        return me.get_value(my_map["table"][pos])

    return None


def remove(my_map, key):
    hash_value = mf.hash_value(my_map, key)

    occupied, pos = find_slot(my_map, key, hash_value)

    if occupied:
        my_map["table"][pos] = me.new_map_entry(None, None)

        my_map["size"] -= 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]

    return my_map


def size(my_map):
    return my_map["size"]


def rehash(my_map):
    old_table = my_map["table"]

    new_capacity = mf.next_prime(my_map["capacity"] * 2)

    my_map["capacity"] = new_capacity
    my_map["table"] = [None] * new_capacity
    my_map["size"] = 0
    my_map["current_factor"] = 0

    for entry in old_table:

        if entry is not None and entry["key"] is not None:
            put(
                my_map,
                me.get_key(entry),
                me.get_value(entry)
            )

    return my_map