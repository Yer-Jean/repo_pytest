def get_val(collection, key, default='git'):
    result = collection.get(key)
    if result:
        return result
    return default
