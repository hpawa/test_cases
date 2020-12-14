def flatter(d, p_key=None, p_d=None, delimeter='.'):
    for k, v in d.items():
        if isinstance(v, dict):
            flatter(v, f'{p_key}{delimeter}{k}' if p_key else k, p_d, delimeter)
        else:
            p_d[f'{p_key}{delimeter}' + k if p_key else k] = v

def value_by_key(d, k):
    return d[k]
