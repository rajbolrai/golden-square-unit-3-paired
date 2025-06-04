def include_to_do(string):
    if len(string) == 0:
        return False
    if "#TODO" in string:
        return True
    return False