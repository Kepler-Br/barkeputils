def human_readable_filesize_base_10(value: int) -> str:
    """
    Returns human-readable file size string.
    WARNING: Units are divided in base 10. Not 2
    :param value: bytes
    :return: formatted string which ends with unit name
    """
    if value < 10 ** 3:
        return f'{value} B'
    if value <= 10 ** 6:
        return f'{value / 10 ** 3:.1f} KB'
    if value <= 10 ** 9:
        return f'{value / 10 ** 6:.1f} MB'
    if value <= 10 ** 12:
        return f'{value / 10 ** 9:.1f} GB'
    if value <= 10 ** 15:
        return f'{value / 10 ** 12:.1f} TB'
    if value <= 10 ** 18:
        return f'{value / 10 ** 15:.1f} PB'
    if value <= 10 ** 21:
        return f'{value / 10 ** 18:.1f} EB'
    if value > 10 ** 21:
        return f'{value / 10 ** 21:.1f} ZB'


def human_readable_filesize_base_2(value: int) -> str:
    """
    Returns human-readable file size string.
    WARNING: Units are divided in base 2
    :param value: bytes
    :return: formatted string which ends with unit name
    """
    if value < 1024:
        return f'{value} B'
    if value <= 1024 ** 2:
        return f'{value / 1024:.1f} KiB'
    if value <= 1024 ** 3:
        return f'{value / 1024 ** 2:.1f} MiB'
    if value <= 1024 ** 4:
        return f'{value / 1024 ** 3:.1f} GiB'
    if value <= 1024 ** 5:
        return f'{value / 1024 ** 4:.1f} TiB'
    if value <= 1024 ** 6:
        return f'{value / 1024 ** 5:.1f} PiB'
    if value <= 1024 ** 7:
        return f'{value / 1024 ** 6:.1f} EiB'
    if value > 1024 ** 8:
        return f'{value / 1024 ** 7:.1f} ZiB'
