def get_val(collection, key, default='git'):
    value = collection.get(key, default)
    return value
