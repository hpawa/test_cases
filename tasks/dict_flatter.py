def flatter(d, p_key=None, p_d=None):
    result = dict()
    if p_d:
        result = {**result, **p_d}
    for k, v in d.items():
        if isinstance(v, dict):
            return flatter(v, f'{p_key}.{k}' if p_key else k, result)
        else:
            result[f'{p_key}.' + k if p_key else k] = v
    return result
