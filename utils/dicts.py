def get_val(collections, key, default='git'):

    if key in collections:
        return collections[key]
    else:
        return default




