from engine.storage.query import table, lookup

def set(entity, component, data):
    lookup[entity].add(component)
    table[component, entity] = data

def unset(entity, component):
    lookup[entity].remove(component)
    del table[component, entity]

set.__doc__ = """
"""
unset.__doc__ = """
"""
