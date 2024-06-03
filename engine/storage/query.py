table = dict()
table["width"] = 0
table["height"] = 0
lookup = table["lookup"] = dict()

def get(entity, datatype):
    return table[datatype, entity]

def entity(index):
    return (table[datatype, index]
        for datatype
        in lookup[index])

def entities(*indices):
    return (entity(index)
        for index
        in indices)

def _retrieve(datatype):
    return (table.get((datatype, entity))
        for entity 
        in range(table["width"]))

def component(datatype):
    return (data
        for data
        in _retrieve(datatype)
        if not data == None)

def components(*datatypes):
    return (data
        for data
        in zip(*(_retrieve(datatype)
            for datatype
            in datatypes))
        if not any((result == None
            for result
            in data)))
     
