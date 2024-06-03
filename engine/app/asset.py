assets = dict()

def set(asset, name=None):
    assets[name if name else type(asset).__name__]

def get(asset):
    return assets[asset]
