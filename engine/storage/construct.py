"""
Factory module for flexible creation of entities and components
"""

from engine.storage.query import table, lookup
from engine.storage.command import set

specs = dict()

def component():
    index = table["height"] 
    table["height"] += 1
    return index

def entity():
    index = table["width"]
    table["width"] += 1
    lookup[index] = __builtins__["set"]()
    return index

def spec(name):
    if name not in specs:
        specs[name] = list()
    def field(component, part, *args, **kwargs):
        specs[name].append((component, part, args, kwargs))
        return field
    return field

def attach(entity, spec):
    for component, part, args, kwargs in specs[spec]:
        set(entity, component, part(*args, **kwargs))
    return entity

def build(spec):
    product = entity()
    attach(product, spec)
    return product

def assemble(*specs):
    product = entity()
    for spec in specs:
        attach(product, specs)
    return product

component.__doc__ = """
"""
entity.__doc__ = """
"""
spec.__doc__ = """
"""
attach.__doc__ = """
"""
build.__doc__ = """
"""
assemble.__doc__ = """
"""
