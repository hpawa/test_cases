def flatter(d, p_key=None, p_d=None):
    for k, v in d.items():
        if isinstance(v, dict):
            flatter(v, f'{p_key}.{k}' if p_key else k, p_d)
        else:
            p_d[f'{p_key}.' + k if p_key else k] = v
