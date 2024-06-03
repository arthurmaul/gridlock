tools = dict()

def set(tool, name=None):
    tools[name if name else tool.__name__] = tool

def get(tool):
    return tools[tool]
