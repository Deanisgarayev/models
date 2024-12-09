def devide(first,second):
    """деления first на second, но когда в second записан 0 - возвращать бесконечность"""
    if second==0:
        return "inf"
    else:
        return first/second