import random

from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
from DataStructures.List import array_list as al


def new_map(num_elements, load_factor, prime=109345121):
    capacity = mf.next_prime(int(num_elements / load_factor))

    table = []
    for _ in range(capacity):
        table.append(al.new_list())

    my_map = {
        "prime": prime,
        "capacity": capacity,
        "scale": random.randint(1, prime - 1),
        "shift": random.randint(0, prime - 1),
        "table": table,
        "current_factor": 0,
        "limit_factor": load_factor,
        "size": 0
    }

    return my_map


def default_compare(key, entry):
    if entry is None:
        return False

    return key == me.get_key(entry)


def put(my_map, key, value):
    pos = mf.hash_value(my_map, key)

    bucket = my_map["table"][pos]

    for entry in bucket["elements"]:
        if default_compare(key, entry):
            me.set_value(entry, value)
            return my_map

    al.add_last(bucket, me.new_map_entry(key, value))

    my_map["size"] += 1
    my_map["current_factor"] = my_map["size"] / my_map["capacity"]

    if my_map["current_factor"] > my_map["limit_factor"]:
        rehash(my_map)

    return my_map


def contains(my_map, key):
    pos = mf.hash_value(my_map, key)

    bucket = my_map["table"][pos]

    for entry in bucket["elements"]:
        if default_compare(key, entry):
            return True

    return False


def get(my_map, key):
    pos = mf.hash_value(my_map, key)

    bucket = my_map["table"][pos]

    for entry in bucket["elements"]:
        if default_compare(key, entry):
            return me.get_value(entry)

    return None


def remove(my_map, key):
    pos = mf.hash_value(my_map, key)

    bucket = my_map["table"][pos]

    for i in range(bucket["size"]):
        entry = bucket["elements"][i]

        if default_compare(key, entry):
            al.delete_element(bucket, i)

            my_map["size"] -= 1
            my_map["current_factor"] = (
                my_map["size"] / my_map["capacity"]
            )

            return my_map

    return my_map


def size(my_map):
    return my_map["size"]


def is_empty(my_map):
    return my_map["size"] == 0


def key_set(my_map):
    keys = al.new_list()

    for bucket in my_map["table"]:
        for entry in bucket["elements"]:
            al.add_last(keys, me.get_key(entry))

    return keys


def value_set(my_map):
    values = al.new_list()

    for bucket in my_map["table"]:
        for entry in bucket["elements"]:
            al.add_last(values, me.get_value(entry))

    return values


def rehash(my_map):
    old_table = my_map["table"]

    new_capacity = mf.next_prime(my_map["capacity"] * 2)

    new_table = []
    for _ in range(new_capacity):
        new_table.append(al.new_list())

    my_map["capacity"] = new_capacity
    my_map["table"] = new_table
    my_map["size"] = 0
    my_map["current_factor"] = 0

    for bucket in old_table:
        for entry in bucket["elements"]:
            put(
                my_map,
                me.get_key(entry),
                me.get_value(entry)
            )

    return my_map