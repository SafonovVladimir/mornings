def list_filtering(mixed_list: list) -> list:
    return [item for item in mixed_list if isinstance(item, int)]
