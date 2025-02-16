def strtobool(val: str):
    return val.strip().lower() in {"y", "yes", "t", "true", "1"}