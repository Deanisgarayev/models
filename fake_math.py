def devide(first,second):
    """деления first на second, но когда в second записан 0 - возвращать строку 'Ошибка'"""
    if second==0:
        return "Ошибка"
    else:
        return first/second