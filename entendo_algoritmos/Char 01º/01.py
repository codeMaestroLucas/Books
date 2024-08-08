def make_bin_search(_list, item: int) -> None:
    _print_result(item= item,
                  pos= _bin_search(_list, item))


def _bin_search(_list: list, item: int) -> int | None:
    start: int = 0
    end: int = len(_list) - 1

    while start <= end:
        middle: int = round((start + end) / 2)
        gess = _list[middle]

        if gess == item:
            return middle  # Position of the item in the list

        elif gess > item:
            end = middle - 1

        else:
            start = middle + 1

    return None  # Not found


def _print_result(item: int, pos: int | None) -> None:
    if pos:
        print(f"The item {item} was founded in the position {pos} of the list.")
        return

    print(f"Didnt find the item {item} in the list.")


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

make_bin_search(l, 1)
